import gevent

# ! gevent is based on greenlet, but can automatically handle switch on IO


def f1():
    print(1)
    gevent.sleep(2)
    print(2)


def f2():
    print(3)
    gevent.sleep(2)
    print(4)


g1 = gevent.spawn(f1)
g2 = gevent.spawn(f2)
print(g1)
print(g2)

gevent.joinall([g1, g2])
