import psutil


class PidService:
    def __init__(self):
        self._container = {}

    @property
    def list(self):
        return self._container.copy()

    def add_pid(self, name, pid):
        if name not in self._container:
            self._container[name] = pid
            return self._container[name]
        else:
            return None

    def get_pid(self, name):
        return self._container.get(name)

    def is_running(self, name):
        return self._container.get(name) is not None

    def kill_all(self):
        for key in self._container:
            # log.warning(f'kill process with pid: {self.get_pid(key)} and name {key}')
            parent = psutil.Process(self.get_pid(key))
            for child in parent.children(recursive=True):
                child.kill()
            parent.kill()

    def kill(self, name):
        if self.is_running(name):
            parent_pid = self.get_pid(name)
            parent = psutil.Process(parent_pid)
            for child in parent.children(recursive=True):
                child.kill()
            parent.kill()
            del self._container[name]
            return parent_pid

        return -1
