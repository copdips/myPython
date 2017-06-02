import time

def timed_sum(a_function):
    def effective_function(n):
        t_0 = time.time()
        a_function(n)
        t_1 = time.time()
        return (int(a_function.__name__[-1], n, t_1 - t_0))
    return effective_function

@timed_sum

def timed_sum_int_1(n):
