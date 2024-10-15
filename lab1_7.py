import asyncio
import time

async def krojenie() -> None:
    await asyncio.sleep(2)
    print("Gotowe krojenie")
async def gotowanie() -> None:
    await asyncio.sleep(5)
    print("Gotowe gotowanie")
async def smazenie() -> None:
    await asyncio.sleep(3)
    print("Gotowe smazenie")
async def main() -> None:
    await asyncio.gather(krojenie(), krojenie(), krojenie())
    await asyncio.gather(krojenie(), gotowanie(), smazenie())
    await asyncio.gather(smazenie(), smazenie(), smazenie())

if __name__ == "__main__":
    start=time.time()
    with asyncio.Runner() as runner:
        runner.run(main())
    print(time.time() - start)
