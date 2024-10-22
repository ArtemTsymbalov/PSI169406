import asyncio
import aiohttp

async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main() -> None:
    cities = {
        "Porlamar": "https://api.open-meteo.com/v1/forecast?latitude=10.9577&longitude=-63.8697&hourly=temperature_2m,wind_speed_10m",
        "Moroni": "https://api.open-meteo.com/v1/forecast?latitude=-11.7022&longitude=43.2551&hourly=temperature_2m,wind_speed_10m",
        "Helsinki": "https://api.open-meteo.com/v1/forecast?latitude=60.1699&longitude=24.9384&hourly=temperature_2m,wind_speed_10m",
        "Kharkov": "https://api.open-meteo.com/v1/forecast?latitude=49.9935&longitude=36.2304&hourly=temperature_2m,wind_speed_10m"
    }

    mask = {"wind_speed_10m": 20}

    tasks = [fetch(url) for url in cities.values()]
    results = await asyncio.gather(*tasks)

    for city, data in zip(cities.keys(), results):
        hourly = data.get("hourly", {})
        wind_speeds = hourly.get("wind_speed_10m", [])
        if all(speed < mask["wind_speed_10m"] for speed in wind_speeds):
            print(f"Прогноз для {city}:")
            print(f"  Prędkość wiatru: {wind_speeds[0]} km/h\n")
            print(data)

if __name__ == "__main__":
    asyncio.run(main())
