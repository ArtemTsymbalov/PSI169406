from dependency_injector.wiring import Provide

import asyncio

from container import Container
from services.iposts_service import IAirQualityService
from utils import consts


async def main(
        service: IAirQualityService = Provide[Container.service],
) -> None:

    titles = await service.get_Titles(consts.SENSOR_ID)
    body = await service.get_Body(consts.SENSOR_ID)


    print(f"{titles[1]},{body[1]}")


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(main())