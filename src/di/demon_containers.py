from dependency_injector import providers, containers
from dependency_injector.containers import DeclarativeContainer

from src.service.pid_service import PidService


class DiDemonContainer(DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["src.controller.views"])

    pid_service = providers.Singleton(
        PidService
    )
