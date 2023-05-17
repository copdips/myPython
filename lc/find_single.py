# the list is sorted, and only one element appears once, the rest appear twice,
# find the element that appears once.
ll = [1, 1, 3, 5, 5, 7, 7, 8, 8]


def find_single(ll):
    if len(ll) == 1:
        return ll[0]
    half = len(ll) // 2
    if ll[half] not in [ll[half - 1], ll[half + 1]]:
        return ll[half]
    elif ll[half] == ll[half - 1]:
        return find_single(
            ll[(half + 1) :] if len(ll[: half - 1]) % 2 == 0 else ll[: half - 1]
        )
    else:
        return find_single(ll[(half + 2) :] if len(ll[:half]) % 2 == 0 else ll[:half])


def find_single2(ll):
    val = None
    while len(ll) > 1:
        half = len(ll) // 2
        print(f"l: {ll}, half: {half}")

        left = half - 1
        right = half + 1
        if ll[half] not in [ll[left], ll[right]]:
            val = ll[half]
            break
        elif ll[half] == ll[left]:
            ll = ll[(half + 1) :] if len(ll[: half - 1]) % 2 == 0 else ll[: half - 1]
        else:
            ll = ll[(half + 2) :] if len(ll[:half]) % 2 == 0 else ll[:half]
    if val is None:
        val = ll[0]
    return val
