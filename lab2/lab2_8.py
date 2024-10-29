import asyncio
import aiohttp
from datetime import datetime, timedelta


async def pobierz_pogode(url, nazwa_miasta):
    async with aiohttp.ClientSession() as sesja:
        async with sesja.get(url) as odpowiedz:
            dane = await odpowiedz.json()
    print(f"Dane otrzymano dla miasta: {nazwa_miasta}")
    return {"miasto": nazwa_miasta, "dane": dane}


async def oblicz_srednia_temperature(dane_miasta):
    temperatury = dane_miasta["dane"]["hourly"]["temperature_2m"]
    czasy = dane_miasta["dane"]["hourly"]["time"]

    # Oblicz następny dzień
    dzisiaj = datetime.now().date()
    jutro = dzisiaj + timedelta(days=1)
    jutro_str = jutro.strftime("%Y-%m-%d")

    suma_temp = 0
    licznik = 0

    for i, czas in enumerate(czasy):
        if czas.startswith(jutro_str):
            suma_temp += temperatury[i]
            licznik += 1

    return {"miasto": dane_miasta["miasto"], "srednia_temp": suma_temp / licznik if licznik else None}


async def main():
    adresy = {
        "Olsztyn": "https://api.open-meteo.com/v1/forecast?latitude=53.7799&longitude=20.4942&hourly=temperature_2m",
        "Charków": "https://api.open-meteo.com/v1/forecast?latitude=49.9935&longitude=36.2304&hourly=temperature_2m",
        "Londyn": "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&hourly=temperature_2m",
        "Tokio": "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m"
    }

    zadania_danych_miast = [pobierz_pogode(url, miasto) for miasto, url in adresy.items()]
    dane_miast = await asyncio.gather(*zadania_danych_miast)

    zadania_srednich_temp = [oblicz_srednia_temperature(dane_miasta) for dane_miasta in dane_miast]
    srednie_temperatury = await asyncio.gather(*zadania_srednich_temp)

    posortowane_miasta = sorted([miasto for miasto in srednie_temperatury if miasto['srednia_temp'] is not None],
                                key=lambda x: x['srednia_temp'], reverse=True)

    prognozy = {miasto['miasto']: miasto['srednia_temp'] for miasto in posortowane_miasta}

    print(prognozy)


if __name__ == "__main__":
    asyncio.run(main())
