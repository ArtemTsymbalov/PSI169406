import asyncio

async def foo1() -> None:
    await asyncio.sleep(1)
    print("Hello world!")
async def foo2() -> None:
    await asyncio.sleep(3)
    print("Hello world!")
async def main() -> None:
    await foo1()
    await foo2()


if __name__ == "__main__":
    with asyncio.Runner() as runner:
        runner.run(main())
