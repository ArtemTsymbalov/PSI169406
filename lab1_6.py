import asyncio
import random


async def fetch(delay: int) -> int:
    await asyncio.sleep(delay)
    r =random.random()
    print(r)
    return r

async def main() -> None:
    await asyncio.gather(fetch(2))
    await asyncio.gather(fetch(3))
    await asyncio.gather(fetch(1))
    print("end!")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)  # 1

    task = loop.create_task(main())  # 2
    loop.run_until_complete(task)  # 3

    pending = asyncio.all_tasks(loop=loop)  # 4
    for pending_task in pending:
        pending_task.cancel()  # 5

    group = asyncio.gather(*pending, return_exceptions=True)  # 6
    loop.run_until_complete(group)  # 7

    loop.close()  # 8