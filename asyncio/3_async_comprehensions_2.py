import asyncio


async def f(x):
    await asyncio.sleep(0.1)
    return x + 100


async def factory(n):
    for x in range(n):
        await asyncio.sleep(0.1)
        yield f, x


async def main():
    # Note that inside the comprehension, the use of await has nothing at all to do with
    # the use of async for: they are doing completely different things and acting
    # on different objects entirely.
    results = [await f(x) async for f, x in factory(3)]
    print("results = ", results)


asyncio.get_event_loop().run_until_complete(main())
# results = [100, 101, 102]
