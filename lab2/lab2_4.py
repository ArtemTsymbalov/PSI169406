import asyncio
import aiohttp

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main() -> None:
    url1 = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    dane = await fetch(url1)
    print(dane)
    hourly = dane.get("hourly", {})
    time = hourly.get("time", [])
    temperature = hourly.get("temperature_2m", [])
    humidity = hourly.get("relative_humidity_2m", [])
    wind_speed = hourly.get("wind_speed_10m", [])
    print(f"Prognoza pogody dla Zakopanego na {time[0]}:")
    print(f"Temperatura: {temperature[0]}°C")
    print(f"Wilgotność: {humidity[0]}%")
    print(f"Prędkość wiatru: {wind_speed[0]} km/h")

if __name__ == "__main__":
    asyncio.run(main())