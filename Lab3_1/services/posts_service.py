from repositories.posts_repository import IAirQualityRepository
from services.iposts_service import IAirQualityService



class AirQualityService(IAirQualityService):
    repository: IAirQualityRepository

    def __init__(self, repository: IAirQualityRepository) -> None:
        self.repository = repository



    async def get_Titles(self, sensor_id: int) -> float:
        all_quality_params = await self.repository.get_all_air_quality_params(sensor_id=sensor_id)
        mean_air_quality_params = [r.title for r in all_quality_params if r.title is not None]

        return mean_air_quality_params

    async def get_Body(self, sensor_id: int) -> float:
        all_quality_params = await self.repository.get_all_air_quality_params(sensor_id=sensor_id)
        mean_air_quality_params = [r.body for r in all_quality_params if r.body is not None]

        return mean_air_quality_params