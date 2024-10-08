async def foo() -> int:
    return 10  # 1


async def main() -> None:
    result = await foo()  # 2
    print(result)  # 3
