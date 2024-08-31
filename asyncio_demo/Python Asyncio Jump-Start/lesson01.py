# SuperFastPython.com
# example of running a coroutine
import asyncio


# define a coroutine
async def custom_coro():
    print("Hello there")


# create the coroutine and run it in the event loop
asyncio.run(custom_coro())
