import asyncio


async def f1():
    print(1)
    await asyncio.sleep(3)
    print(2)
    return "f1"


async def f2():
    print(3)
    await asyncio.sleep(3)
    print(4)
    return "f2"


async def main():
    group1 = asyncio.gather(f1(), f1())
    group2 = asyncio.gather(f2(), f2())
    group1.cancel()
    all_groups = await asyncio.gather(group1, group2, return_exceptions=True)
    print(all_groups)


asyncio.run(main())
