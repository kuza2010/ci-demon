import atexit
import json
import sys
from logging.config import dictConfig

from flask import Flask, request, jsonify

from src.controller.views import service_api
from src.di.demon_containers import DiDemonContainer
from src.service.pid_service import PidService
from src.service.shutdown_service import close_service


def create_app(configfile, **kwargs):
    """
       Entry point to the CI-DEMON
    """
    from flask import current_app

    # configure log
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['stdout']
        }
    })

    # configure di container
    container = DiDemonContainer()

    app = Flask(__name__, **kwargs)
    app.config.from_file(configfile, load=json.load)
    app.container = container
    app.register_blueprint(service_api)

    @app.before_request
    def before_request():
        token = request.headers.get('token')
        if token is None or token != current_app.config['AUTH']['TOKEN']:
            return jsonify(ok='nok'), 401

    def provider() -> PidService:
        return app.container.pid_service()

    atexit.register(close_service, provider)

    return app


def main():
    config_path = sys.argv[1]
    app = create_app(configfile=config_path)
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
