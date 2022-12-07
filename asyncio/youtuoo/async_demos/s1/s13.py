import asyncio


async def f1():
    await asyncio.sleep(3)
    return 111


async def f2():
    return 222


async def main():
    tasks = [
        asyncio.create_task(f1()),
        asyncio.create_task(f2()),
    ]

    done, pending = await asyncio.wait(tasks, timeout=1)
    for d in done:
        print(d.result())
    for p in pending:
        print(p)
    # await asyncio.gather(
    #     asyncio.create_task(f1()),
    #     f2()
    # )

    # rets = await asyncio.gather(*tasks)
    # print(rets)


asyncio.run(main())
