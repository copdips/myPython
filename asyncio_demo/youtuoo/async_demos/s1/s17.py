import asyncio


async def set_result(fut):
    await asyncio.sleep(2)
    fut.set_result("xxx")


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()

    task = asyncio.create_task(set_result(fut))

    data = await asyncio.gather(fut, task)
    print(data)


asyncio.run(main())
