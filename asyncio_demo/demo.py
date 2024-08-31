import asyncio


async def main():
    await asyncio.sleep(5)
    # await asyncio.sleep(5)
    print("hello")


# asyncio.run(main()) runs top of sth. like:
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
asyncio.run(main())
