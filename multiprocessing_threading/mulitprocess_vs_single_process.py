# Gao Tian 我用了多进程怎么程序反而变慢了: https://www.youtube.com/watch?v=xFtEg_e54as
import multiprocessing
import time

MAX_NUMBER = 100000
WORKERS_COUNT = 4


def is_prime(n):
    return False if n <= 1 else all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def single_process():
    primes = []

    start = time.time()
    primes = [i for i in range(1, MAX_NUMBER) if is_prime(i)]

    print(f"Single process time taken: {time.time() - start} seconds")
    print(f"Number of primes: {len(primes)}")


def multi_process():
    primes = []

    def worker(inq, outq):
        while n := inq.get():
            if is_prime(n):
                outq.put(n)
        outq.put(None)

    start = time.time()

    inq = multiprocessing.Queue()
    outq = multiprocessing.Queue()

    workers = [
        multiprocessing.Process(target=worker, args=(inq, outq))
        for _ in range(WORKERS_COUNT)
    ]

    for w in workers:
        w.start()

    for i in range(1, MAX_NUMBER):
        inq.put(i)

    for _ in workers:
        inq.put(None)

    finish = 0
    while finish < WORKERS_COUNT:
        if n := outq.get():
            primes.append(n)
        else:
            finish += 1

    print(f"Multi process time taken: {time.time() - start} seconds")
    print(f"Number of primes: {len(primes)}")


def multi_process_with_slice():
    primes = []

    def worker(inq, outq):
        while vals := inq.get():
            start, end = vals
            primes = [n for n in range(start, end) if is_prime(n)]
            outq.put(primes)
        outq.put(None)

    start = time.time()

    inq = multiprocessing.Queue()
    outq = multiprocessing.Queue()

    workers = [
        multiprocessing.Process(target=worker, args=(inq, outq))
        for _ in range(WORKERS_COUNT)
    ]

    for w in workers:
        w.start()

    for i in range(WORKERS_COUNT):
        inq.put(
            (i * MAX_NUMBER // WORKERS_COUNT, (i + 1) * MAX_NUMBER // WORKERS_COUNT)
        )

    for _ in workers:
        inq.put(None)

    finish = 0
    while finish < WORKERS_COUNT:
        if n := outq.get():
            primes.extend(n)
        else:
            finish += 1

    print(f"Multi process with slice time taken: {time.time() - start} seconds")
    print(f"Number of primes: {len(primes)}")


def multi_process_with_pool():
    start = time.time()
    with multiprocessing.Pool(WORKERS_COUNT) as pool:
        primes = [
            n + 1
            for n, prime in enumerate(pool.map(is_prime, range(1, MAX_NUMBER)))
            if prime
        ]
    print(f"Multi process with pool time taken: {time.time() - start} seconds")
    print(f"Number of primes: {len(primes)}")


single_process()
multi_process()
multi_process_with_slice()
multi_process_with_pool()
