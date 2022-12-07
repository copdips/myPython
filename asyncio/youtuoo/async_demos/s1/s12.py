import asyncio


async def f1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def f2():
    print(3)
    await asyncio.sleep(2)
    print(4)


async def main():
    tasks = [
        asyncio.create_task(f1()),
        asyncio.create_task(f2()),
    ]
    await asyncio.wait(tasks)


asyncio.run(main())
