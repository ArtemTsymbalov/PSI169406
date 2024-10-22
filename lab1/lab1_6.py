import asyncio
import random
import time

async def fetch(delay: int) -> float:
    await asyncio.sleep(delay)
    r =random.random()
    print(r)
    return r

async  def main() -> None:
    await asyncio.gather(fetch(2), fetch(1), fetch(3))

if __name__ == "__main__":
    start=time.time()
    with asyncio.Runner() as runner:
        runner.run(main())
    print(time.time() - start)
