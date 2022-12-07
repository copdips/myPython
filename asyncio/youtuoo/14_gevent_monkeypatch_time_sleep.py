import time

import gevent
from gevent import monkey

# ! time.sleep is patched by gevent to be asyncable
monkey.patch_all()


def f1():
    print(1)
    time.sleep(2)
    print(2)


def f2():
    print(3)
    time.sleep(2)
    print(4)


g1 = gevent.spawn(f1)
g2 = gevent.spawn(f2)
print(g1)
print(g2)

gevent.joinall([g1, g2])
