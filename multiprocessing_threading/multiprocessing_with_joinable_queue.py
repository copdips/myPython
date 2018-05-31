# https://blog.csdn.net/tyq101010/article/details/72628925

# multiprocessing是python标准库中支持多进程并发的模块，我们这里采用multiprocessing中的数据结构：JoinableQueue，它本质上仍是一个FIFO的队列，它与一般队列（如queue中的Queue)的区别在于它是多进程安全的，这意味着我们不用担心它的互斥和死锁问题。JoinableQueue主要可以用来存放执行的任务和收集任务的执行结果。

import multiprocessing
import random
import time

def read(q):
    while True:
        try:
            value = q.get()
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        finally:
            q.task_done()

def main():
    q = multiprocessing.JoinableQueue()
    pw1 = multiprocessing.Process(target=read, args=(q,))
    pw2 = multiprocessing.Process(target=read, args=(q,))

    # 将子进程设置为守护进程——主进程结束后随之结束
    pw1.daemon = True
    pw2.daemon = True

    # 子进程就开始独立于父进程运行
    pw1.start()
    pw2.start()
    for c in [chr(ord('A') + i) for i in range(26)]:
        # q是一个JoinableQueue对象，支持get方法读取第一个元素，如果q中没有元素，进程就会阻塞，直至q中被存入新元素
        q.put(c)
        # 26个字母依次放入JoinableQueue对象中，这时候两个子进程不再阻塞，开始真正地执行任务。两个子进程都用value = q.get()来读取数据，它们都在修改q对象，而我们并不用担心同步问题，这就是multiProcessing.Joinable数据结构的优势所在——它是多进程安全的，它会自动处理“加锁”的过程。
    try:
        # q.join()方法会查询q中的数据是否已读完——这里指的就是任务是否执行完，如果没有，程序会阻塞住等待q中数据读完才开始继续执行（可以用Ctrl+C强制停止
        q.join()
    except KeyboardInterrupt:
        print("stopped by hand")

if __name__ == '__main__':
    main()
