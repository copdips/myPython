#  calc fib(n) = fib(n-1) + fib(n-2)
# [(1, 0), (2, 1), (3, 1), (4, 2), (5, 3), (6, 5), (51, 12586269025), (101, 354224848179261915075)]
from functools import lru_cache

import pytest


@lru_cache()
def fib1(n):
    return n - 1 if n < 3 else fib1(n - 1) + fib1(n - 2)


def fib2(n):
    if n < 3:
        return n - 1
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (6, 5),
        (51, 12586269025),
        (101, 354224848179261915075),
    ],
)
def test_fib(n, expected):
    print(f"{fib1(n)}")
    assert expected == fib1(n)
    assert expected == fib2(n)
