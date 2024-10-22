import asyncio

async def Fibo(n):
    a , b = 1, 1
    for i in range(n):
        print(a, end=' ')
        b += a
        a = b - a
        await asyncio.sleep(1)
async def main() -> None:  # 1
    n=int(input())
    await Fibo(n)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    task = loop.create_task(main())  # 2

    try:
        loop.run_until_complete(task)  # 3
    except KeyboardInterrupt:  # 4
        print("Closing the app")

        tasks = asyncio.all_tasks(loop=loop)  # 5
        for task_ in tasks:
            task_.cancel()

        group = asyncio.gather(*tasks, return_exceptions=True)
        loop.run_until_complete(group)
        loop.close()