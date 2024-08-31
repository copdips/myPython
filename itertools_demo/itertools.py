def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i * n : (i + 1) * n]) for i in range(num_groups)]


def naive_grouper_wo_tuple(inputs, n):
    num_groups = len(inputs) // n
    return ((inputs[i * n : (i + 1) * n]) for i in range(num_groups))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
naive_grouper_wo_tuple(nums, 2)
