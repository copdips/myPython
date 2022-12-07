# https://blog.csdn.net/tyq101010/article/details/72628925
import queue
import random
import threading
import time
from multiprocessing import Manager, Process, cpu_count


def read(q):
    while True:
        try:
            value = q.get()
            print("Get %s from queue." % value)
            time.sleep(random.random())
        finally:
            q.task_done()


def main():
    # 多线程与多进程基本一致，只是这里我们不必使用multiProcessing.JoinableQueue对象了，一般的队列（来自queue.Queue)就可以满足要求
    q = queue.Queue()
    pw1 = threading.Thread(target=read, args=(q,))
    pw2 = threading.Thread(target=read, args=(q,))
    pw1.daemon = True
    pw2.daemon = True
    pw1.start()
    pw2.start()
    for c in [chr(ord("A") + i) for i in range(26)]:
        q.put(c)
    try:
        q.join()
    except KeyboardInterrupt:
        print("stopped by hand")


if __name__ == "__main__":
    main()
