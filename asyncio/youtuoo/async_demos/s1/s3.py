def f1():
    yield 1
    yield from f2()
    yield 2


def f2():
    yield 3
    yield 4


g = f1()

for i in g:
    print(i)
