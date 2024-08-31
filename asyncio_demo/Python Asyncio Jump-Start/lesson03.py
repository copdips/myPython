# SuperFastPython.com
# example of running many coroutines concurrently
import asyncio
import random


# coroutine to perform some useful task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random.random()
    # suspend and sleep for a moment
    await asyncio.sleep(value)
    # report the argument and value
    print(f"Task {arg} done after {value} seconds")


# main coroutine
async def main():
    # create many coroutines
    coros = [task_coro(i) for i in range(100)]
    # suspend and run all coroutines
    await asyncio.gather(*coros)


# create the coroutine and run it in the event loop
asyncio.run(main())
