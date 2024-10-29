from abc import ABC


class IAirQualityService(ABC):
    async def get_air_quality_index(self, sensor_id: int) -> str:
        pass

    async def get_Titles(self, sensor_id: int) -> float:
        pass