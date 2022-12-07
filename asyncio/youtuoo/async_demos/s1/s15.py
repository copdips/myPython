import asyncio
from asyncio import Future
from functools import partial


async def f1():
    await asyncio.sleep(2)
    return "f1"


def callback1(future: Future):
    print(future.result())
    print("我是f1的回调函数")


def callback2(t1, future: Future):
    print(t1)
    print(future.result())


async def main():

    task1 = asyncio.create_task(f1())
    task1.add_done_callback(callback1)  # 给task1绑定了一个回调函数
    # task1.add_done_callback(partial(callback2, "这是t1参数"))
    # await task1

    tasks = [task1]

    await asyncio.wait(tasks)


asyncio.run(main())
