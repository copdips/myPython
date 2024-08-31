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
    print("main start")

    tasks = [
        asyncio.create_task(f1()),
        asyncio.create_task(f2()),
    ]

    print(1111)

    await asyncio.wait(tasks)

    print("main end")


asyncio.run(main())
