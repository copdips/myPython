import asyncio


async def f1():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return 123


async def f2():
    print(3)
    await asyncio.sleep(2)
    print(4)
    return 456


async def main():
    print("main start")
    res1 = await f1()  # 等f1执行后再执行f2, 因为目前事件循环中只有一个任务（main）
    print(res1)
    res2 = await f2()
    print(res2)
    print("main end")


asyncio.run(main())
