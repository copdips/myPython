# SuperFastPython.com
# example of sharing data between coroutines using a queue
import asyncio
from random import random


# coroutine to generate work
async def producer(queue):
    print("Producer: Running")
    # generate work
    for i in range(10):
        # generate a value between 0 and 1
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print("Producer: Done")


# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the consumer as an independent task
    asyncio.create_task(producer(queue))
    # consume items from the queue until a None is seen
    while True:
        # get a value from the queue
        value = await queue.get()
        # check for a "no more data" value
        if not value:
            break
        # report the value
        print(f"Got: {value}")


# start the asyncio program
asyncio.run(main())
