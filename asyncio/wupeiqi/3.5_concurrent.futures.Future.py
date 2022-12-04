# standard usage of concurrent.futures.Future by multithreading or multiprocess
import time
from concurrent.futures import Future
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor


def func(value):
    time.sleep(1)
    print(value)
    return value


# create thread pool
pool = ThreadPoolExecutor(max_workers=5)

# or create process pool
# pool = ProcessPoolExecutor(max_workers=5)

for i in range(10):
    # fut is a concurrent.futures.Future object, but not asyncio.Future object.
    # 10 threads were created, but with real asyncio compatible module, there'll be only one thread created.
    fut = pool.submit(func, i)
    print(fut)
