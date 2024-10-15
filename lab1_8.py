import asyncio
import time

async def przetwarzanie(plik)-> None:
    print("Starting to load file", plik)
    await asyncio.sleep(2)
    print("File loaded", plik)

    print("Starting to analyze file", plik)
    await asyncio.sleep(4)
    print("File analyzed", plik)

    print("Starting to save file", plik)
    await asyncio.sleep(1)
    print("File saved", plik)

async def main()-> None:
        tasks = []
        for i in range(5):
            tasks.append(przetwarzanie(i))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.time()
    with asyncio.Runner() as runner:
        runner.run(main())
    print(time.time() - start)