from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import sleep
from typing import Callable, Iterator

import numpy as np
from stopwatch import Stopwatch

TEST_COUNT = 100
LENGTH = 50_000_000


# CPU bounded
def generate_random_bytes(length: int) -> bytearray:
    # faster with multiprocessing as len() returns a small value that is easy to serialize between processes
    return [len(np.random.bytes(length))]
    # faster with multithreading as bytes is a big value that takes time to serialize between processes
    return [np.random.bytes(length)]


def sum_lengths(ite: Iterator) -> int:
    total_length = 0
    for data in ite:
        total_length += len(data)

    return total_length


def run_in_pool(pool_factory: Callable, workers: int):
    pool = pool_factory(max_workers=workers)

    with Stopwatch(name=f"{pool_factory.__name__} ({workers})", print_report=True):
        results = pool.map(generate_random_bytes, [LENGTH] * TEST_COUNT)
        total_length = sum_lengths(results)
        print(f"Total bytes: {total_length}")

    pool.shutdown()


def main():
    # Test 1: 16 concurrent processes
    run_in_pool(ProcessPoolExecutor, 16)
    sleep(5)

    # Test 2: 2 concurrent threads
    run_in_pool(ThreadPoolExecutor, 2)
    sleep(5)

    # Test 3: 16 concurrent threads
    run_in_pool(ThreadPoolExecutor, 16)
    sleep(5)

    # Test 4: Single thread, single process for reference
    with Stopwatch(name="Mono thread", print_report=True):
        results = (generate_random_bytes(LENGTH) for _ in range(TEST_COUNT))
        total_length = sum_lengths(results)
        print(f"Total bytes: {total_length}")


if __name__ == "__main__":
    main()
