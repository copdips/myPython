# show internals of asyncio.Future, normally we never use it directly
import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result("666")


async def main():
    loop = asyncio.get_event_loop()

    # create a task (Future object), but without definition, so this task will never know when it will be finished
    # ! with asyncio.create_task(func(), name="func1"), a task has always a defined function, so will be finished for sure. But not the case for loop.create_future().
    # ! normally, we never use loop.create_future() directly, always use asyncio.create_task(func(), name="func1")
    fut = loop.create_future()

    # without this task added into loop, the function will never stop, as fut never get output.
    await loop.create_task(set_after(fut))

    #  wait fut output, otherwise keep waiting
    data = await fut
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
