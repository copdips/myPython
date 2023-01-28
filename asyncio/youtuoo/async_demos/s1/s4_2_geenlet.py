from greenlet import greenlet

# ! greenlet could switch but dont know when to switch especially when there's an IO


def f1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()


def f2():
    print(3)
    gr1.switch()
    print(4)
    gr1.switch()


gr1 = greenlet(f1)
gr2 = greenlet(f2)

gr1.switch()
