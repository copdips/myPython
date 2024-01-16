# https://superfastpython.com/asyncio-log-blocking/

# SuperFastPython.com
# example of asyncio logging is blocking
import asyncio
import logging
from random import random


# helper function to setup the logger
def init_logger():
    # get the root logger
    log = logging.getLogger()
    # log all messages, debug and up
    log.setLevel(logging.DEBUG)


# task that does work and logs
async def task(value):
    # log a message
    logging.info(f"Task {value} is starting")
    # simulate doing work
    await asyncio.sleep(random() * 5)
    # log a message
    logging.info(f"Task {value} is done")


# main coroutine
async def main():
    # initialize the logger
    init_logger()
    # log a message
    logging.info(f"Main is starting")

    # issue many tasks
    async with asyncio.TaskGroup() as group:
        for i in range(10):
            _ = group.create_task(task(i))
    # tasks = [asyncio.create_task(task(i)) for i in range(10)]
    # await asyncio.gather(*tasks)

    # log a message
    logging.info(f"Main is done")


# start the event loop
asyncio.run(main())
