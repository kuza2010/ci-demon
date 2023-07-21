import atexit
from logging.config import dictConfig

from flask import Flask

from src.controller.views import service_api
from src.di.demon_containers import DiDemonContainer
from src.service.pid_service import PidService
from src.service.shutdown_service import close_service


def create_app(**kwargs):
    """
       Entry point to the CI-DEMON
    """

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
    app.container = container
    app.register_blueprint(service_api)

    def provider() -> PidService:
        return app.container.pid_service()

    atexit.register(close_service, provider)

    return app
