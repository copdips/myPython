import asyncio
from asyncio import Future


async def f1():
    await asyncio.sleep(2)
    print("f1")
    return "f1"


def callback(future: Future):
    future.get_loop().stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(f1())  # 这个事件循环不会一直运行，会在f1运行结束会结束事件循环。


# loop = asyncio.get_event_loop()

# task1 = asyncio.ensure_future(f1())
# task1.add_done_callback(callback)

# loop.run_forever()
