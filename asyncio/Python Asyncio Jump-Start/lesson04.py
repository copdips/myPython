# SuperFastPython.com
# example of waiting for a collection of tasks
import asyncio
import random


# coroutine to perform some useful task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random.random()
    # suspend and sleep for a moment
    await asyncio.sleep(value)
    # return a value unique for this task
    return arg * value


# main coroutine
async def main():
    # create and schedule many independent tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(100)]
    # suspend and wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # report the result from the first task
    task = done.pop()
    print(f"First task got: {task.result()}")


# create the coroutine and run it in the event loop
asyncio.run(main())
