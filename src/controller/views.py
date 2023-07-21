from dependency_injector.wiring import Provide, inject
from flask import Blueprint, jsonify

from src.di.demon_containers import DiDemonContainer
from src.service.pid_service import PidService
from src.service.runners import TransliterateBotRunner

service_api = Blueprint('service_api', __name__)


@service_api.route('/bot', methods=["GET"])
@inject
def get_all(
        pid_service: PidService = Provide[DiDemonContainer.pid_service]
):
    return jsonify(pid_list=pid_service.list)


@service_api.route('/bot/<name>', methods=['GET'])
@inject
def get_running_bot(
        name,
        pid_service: PidService = Provide[DiDemonContainer.pid_service]
):
    return jsonify(
        name=name,
        id=pid_service.get_pid(name)
    )


@service_api.route('/bot/<name>', methods=['POST'])
@inject
def run_bot(
        name,
        pid_service: PidService = Provide[DiDemonContainer.pid_service]
):
    if name != 'transliterate_bot':
        return jsonify(ok='nok'), 404

    if pid_service.is_running(name) is False:
        try:
            runner = TransliterateBotRunner()
            pid = runner.do_run()
            pid_service.add_pid(runner.name, pid)
            return jsonify(ok='ok', id=pid), 201
        except Exception as e:
            print(e)
            return jsonify(ok='nok', reason='Can not run the bot'), 500
    else:
        return jsonify(ok='nok'), 304


@service_api.route('/bot/<name>', methods=['DELETE'])
@inject
def stop_bot(
        name,
        pid_service: PidService = Provide[DiDemonContainer.pid_service]
):
    pid = +pid_service.kill(name)
    return jsonify(ok='ok', id=pid), 200
