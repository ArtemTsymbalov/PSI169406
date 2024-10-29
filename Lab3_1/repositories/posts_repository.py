import aiohttp

from typing import Iterable

from utils import consts
from domains.posts import PostRecord
from repositories.iposts_repository import IAirQualityRepository


class AirQualityRepository(IAirQualityRepository):
    async def get_last_air_quality_params(self, sensor_id: int) -> PostRecord | None:
        all_params = await self._get_params(sensor_id)
        parsed_params = await self._parse_params(all_params)

        return parsed_params[0]

    async def get_all_air_quality_params(self, sensor_id: int) -> Iterable[PostRecord] | None:
        all_params = await self._get_params(sensor_id)
        parsed_params = await self._parse_params(all_params)

        return parsed_params

    async def _get_params(self, sensor_id: int) -> Iterable[dict] | None:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_SENSOR_URL.format(sensor_id=sensor_id)) as response:
                if response.status != 200:
                    return None

                return await response.json()

    async def _parse_params(self, params: Iterable[dict]) -> Iterable[PostRecord]:
        return [PostRecord(userId=record.get("userId"), id=record.get("id"), title=record.get("title"),body=record.get("body")) for record in
                params]