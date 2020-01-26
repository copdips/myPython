def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]


for _ in naive_grouper(range(100000000), 10):
    pass


def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

for _ in better_grouper(range(100000000), 10):
    pass
