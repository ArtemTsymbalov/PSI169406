from dependency_injector import containers, providers

from repositories.posts_repository import AirQualityRepository
from services.posts_service import AirQualityService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repository = providers.Singleton(
        AirQualityRepository,
    )

    service = providers.Factory(
        AirQualityService,
        repository=repository,
    )