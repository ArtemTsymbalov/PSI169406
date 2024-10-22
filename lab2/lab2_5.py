import asyncio
import aiohttp


async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_weather_data() -> dict:
    cities = {
        "Porlamar": "https://api.open-meteo.com/v1/forecast?latitude=10.9577&longitude=-63.8697&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current_weather=true",
        "Moroni": "https://api.open-meteo.com/v1/forecast?latitude=-11.7022&longitude=43.2551&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current_weather=true",
        "Helsinki": "https://api.open-meteo.com/v1/forecast?latitude=60.1699&longitude=24.9384&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current_weather=true"
    }
    tasks = [fetch(url) for url in cities.values()]
    results = await asyncio.gather(*tasks)

    weather_data = {city: result for city, result in zip(cities.keys(), results)}
    return weather_data


async def main() -> None:
    weather_data = await get_weather_data()

    for city, data in weather_data.items():
        hourly = data.get("hourly", {})
        time = hourly.get("time", [])
        temperature = hourly.get("temperature_2m", [])
        humidity = hourly.get("relative_humidity_2m", [])
        wind_speed = hourly.get("wind_speed_10m", [])

        print(f"Prognoza pogody dla {city} na {time[0]}:")
        print(f"  Temperatura: {temperature[0]} C")
        print(f"  Wilgotność: {humidity[0]}%")
        print(f"  Prędkość wiatru: {wind_speed[0]} km/h\n")


if __name__ == "__main__":
    asyncio.run(main())
