import asyncio


async def f1():
    print(123)
    await asyncio.sleep(2)
    print(456)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(f1())

asyncio.run(f1())
