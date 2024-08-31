import asyncio
import time


async def f1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def f2():
    print(3)
    await asyncio.sleep(2)
    print(4)


async def main():
    start = time.time()
    # await f1()
    # await f2()

    tasks = [
        asyncio.create_task(f1()),
        asyncio.create_task(f2()),
    ]
    await asyncio.wait(tasks)

    print(time.time() - start)


asyncio.run(main())
