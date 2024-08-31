import asyncio


def g():
    print(1)
    await asyncio.sleep(2)


g()


async def f1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def f2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [asyncio.ensure_future(f1()), asyncio.ensure_future(f2())]

loop = asyncio.get_event_loop()  # 获取一个事件循环
loop.run_until_complete(asyncio.wait(tasks))
