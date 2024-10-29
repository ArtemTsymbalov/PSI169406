from abc import ABC
from typing import Iterable

from domains.posts import PostRecord


class IAirQualityRepository(ABC):
    async def get_last_air_quality_params(self, sensor_id: int) -> PostRecord | None:
        pass

    async def get_all_air_quality_params(self, sensor_id: int) -> Iterable[PostRecord] | None:
        pass