from threading import Thread
#!/usr/bin/python
from multiprocessing import cpu_count, Process,Manager
import time
from timeit import timeit


cpu_count = cpu_count()

def count(n):
    ''' for mass IO, multithreading is better
    '''
    time.sleep(0.5)
    while n > 0:
        n -= 1


# def count(n):
#     ''' for mass calc, multiprocess is better
#         but dont surpass cpu core number
#     '''
#     while n > 0:
#         n -= 1


def test_normal():
    for i in range(cpu_count-1):
        count(1000000)
        time.sleep(0.5)


def test_Thread():
    l = []
    for i in range(cpu_count-1):
        p = Thread(target=count,args=(1000000,))
        l.append(p)
        p.start()
    for j in l:
        j.join()


def test_Process():
    l = []
    for i in range(cpu_count-1):
        p = Process(target=count,args=(1000000,))
        l.append(p)
        p.start()
    for j in l:
        j.join()


if __name__ == '__main__':
    print("test_normal")
    r = timeit('test_normal()', 'from __main__ import test_normal', number=10)
    print(r)

    print("test_Thread")
    r = timeit('test_Thread()', 'from __main__ import test_Thread', number=10)
    print(r)

    print("test_Process")
    r = timeit('test_Process()', 'from __main__ import test_Process', number=10)
    print(r)
