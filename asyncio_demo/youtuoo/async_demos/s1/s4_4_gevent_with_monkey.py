import time

import gevent
from gevent import monkey

monkey.patch_all()


def f1():
    print(1)
    # gevent.sleep(2)        # 注意不使用time.sleep(2)
    time.sleep(2)
    print(2)


def f2():
    print(3)
    # gevent.sleep(2)
    time.sleep(2)
    print(4)


g2 = gevent.spawn(f2)
g1 = gevent.spawn(f1)


gevent.joinall([g1, g2])  # 程序就会在这个地方停住，等待g1、g2执行结束再往下运行

print("主程序结束了...")
