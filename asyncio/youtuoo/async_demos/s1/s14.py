import asyncio


async def f1():
    await asyncio.sleep(2)
    return "f1"


async def f2():
    await asyncio.sleep(2)
    return "f2"


async def main():
    tasks = [
        asyncio.create_task(f1(), name="f1"),
        asyncio.create_task(f2(), name="f2"),
        asyncio.ensure_future(f1()),
    ]
    done, _ = await asyncio.wait(tasks)
    for d in done:
        print(d.get_name())
        print(d)


asyncio.run(main())
