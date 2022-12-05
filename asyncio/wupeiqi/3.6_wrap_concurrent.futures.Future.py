# wrap non asyncio compatible module in asyncio with concurrent.futures.Future
# https://docs.python.org/3/library/asyncio-eventloop.html?highlight=run_in_executor#executing-code-in-thread-or-process-pools
import asyncio
import concurrent.futures
import functools


def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    # blocking_io() is like func() (from 3.5_concurrent.futures.Future.py), which is not asyncio func, was run by multithreading or multiprocessing
    # this time, we'll run it in asyncio
    with open("/dev/urandom", "rb") as f:
        return f.read(10)


def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10**7))


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(functools.partial(print, "Hello", flush=True))

    # 1. run_in_executor() default executer is ThreadPoolExecutor, so None here
    # https://github.com/python/cpython/blob/854a878e4f09cd961ba5135567f7a5b5f86d7be9/Lib/asyncio/base_events.py#L834-L835

    # Internals:
    # Step 1: call the submit() of ThreadPoolExecutor to use a thread from the thread pool to execute func, and return a concurrent.futures.Future object.
    # https://github.com/python/cpython/blob/854a878e4f09cd961ba5135567f7a5b5f86d7be9/Lib/asyncio/base_events.py#L840

    # Step 2: Use asyncio.warp_future to wrap a concurrent.futures.Future object into a asyncio.Future object.
    # This is because we cannot use await concurrent.futures.Future, await accepts only 3 types: collections.abc.Coroutine, asyncio.Task, asyncio.Future
    # https://github.com/python/cpython/blob/854a878e4f09cd961ba5135567f7a5b5f86d7be9/Lib/asyncio/base_events.py#L839
    fut = loop.run_in_executor(None, blocking_io)
    result = await fut
    print(f"default thread pool result: {result}")

    # 2. Run in a custom thread pool
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io)
        print(f"custom thread pool result: {result}")

    # 3. Run in a custom process pool
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound)
        print(f"custom process pool result: {result}")


asyncio.run(main())
