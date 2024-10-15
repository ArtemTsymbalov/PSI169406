import asyncio
import time

async def machine_a(times)-> None:
    for i in range(times):
        print("Machine A starts operation", i)
        await asyncio.sleep(2)
        print("Machine A finished operation")


async def machine_b(times)-> None:
    for i in range(times):
        print("Machine B starts operation", i)
        await asyncio.sleep(3)
        print("Machine B finished operation")


async def machine_c(times)-> None:
    for i in range(times):
        print("Machine C starts operation", i)
        await asyncio.sleep(5)
        print("Machine C finished operation")


async def main()-> None:
    await asyncio.gather(machine_a(7), machine_b(5), machine_c(3))


if __name__ == "__main__":
    start=time.time()
    with asyncio.Runner() as runner:
        runner.run(main())
    print(time.time()-start)
