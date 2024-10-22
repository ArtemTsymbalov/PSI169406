import asyncio
import aiohttp

async def fetch(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main() -> None:
    urls = [
        "https://www.valvesoftware.com/about/stats",
        "https://www.dnd5eapi.co/api/ability-scores/cha",
        "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1",
        "https://api.tcgdex.net/v2/en/cards/swsh3-136",
        "https://api.tcgdex.net/v2/en/cards/swsh3-135"
    ]
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for result in enumerate(results):
        print(result)

if __name__ == "__main__":
    asyncio.run(main())