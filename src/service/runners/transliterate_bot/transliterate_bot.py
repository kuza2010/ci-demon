import os
import subprocess
import time

from flask import current_app

from src.service.runners import BaseRunner
from src.service.runners.exception import RunnerException


class TransliterateBotRunner(BaseRunner):
    def __init__(self):
        self._name = 'transliterate_bot'

        absolute_path = os.path.dirname(__file__)
        relative_path = self.name + '.sh'
        self._full_path = os.path.join(absolute_path, relative_path)

    @property
    def name(self):
        return self._name

    @property
    def full_path(self):
        return self._full_path

    def do_run(self):
        child_proc = subprocess.Popen([
            self.full_path,
            current_app.config['TRANSLITERATE_BOT']['TG_TOKEN'],
            current_app.config['TRANSLITERATE_BOT']['BOT_FOLDER'],
            current_app.config['TRANSLITERATE_BOT']['MAIN_EXECUTABLE_FILE'],
        ], stdout=subprocess.PIPE)
        try:
            child_proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            child_proc.kill()
            raise RunnerException('Timeout exceeded')

        pid = self.__check_pid(child_proc)

        if pid == -1:
            child_proc.kill()
            raise RunnerException('Can not determine main pid')

        return pid

    # block readline
    def __check_pid(self, proc):
        max_time = time.time() + 10

        while time.time() < max_time:
            line = proc.stdout.readline().decode("utf-8")
            print(line)
            if line.startswith('MAIN_PID:'):
                pid = int(line.replace('MAIN_PID:', ''))
                # log.info(f'{self.name} started with pid: {pid}')
                return pid

        return -1
