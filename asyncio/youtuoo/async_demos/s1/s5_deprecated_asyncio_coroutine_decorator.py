import asyncio


@asyncio.coroutine
def f1():
    print(1)
    yield from asyncio.sleep(4)
    print(2)


@asyncio.coroutine
def f2():
    print(3)
    yield from asyncio.sleep(4)
    print(4)


print(f1())

tasks = [asyncio.ensure_future(f1()), asyncio.ensure_future(f2())]
#  ! or without asyncio.ensure_future()
# tasks = [f1(), f2()]

loop = asyncio.get_event_loop()  # 获取一个事件循环
loop.run_until_complete(asyncio.wait(tasks))
