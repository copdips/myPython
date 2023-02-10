# SuperFastPython.com
# example of waiting for a collection of tasks
import asyncio
import random


# coroutine to perform some useful task
async def task_coro(arg):
    # generate a random value between 0 and 10
    value = random.random() * 10
    # suspend and sleep for a moment
    await asyncio.sleep(value)
    # return a value unique for this task
    return arg * value


# main coroutine
async def main():
    # create and schedule many independent tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(100)]
    # handle tasks in completion order
    for task in asyncio.as_completed(tasks):
        # suspend and get the result from the task
        result = await task
        # report the task result
        print(f"> got {result}")


# create the coroutine and run it in the event loop
asyncio.run(main())
