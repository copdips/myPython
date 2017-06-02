def digits(x) :
    """ natural integer x """

    digs = []
    if x == 0 :
        digs=[0]
    while (x != 0) :
        div, mod = divmod(x, 10)
        digs.append(mod)
        x = div
    return digs

def is_palindrome(x) :
    """ natural integer x """

    if (x < 0):
        return False
    print("\ninput :", x)
    digs = digits(x)
    print("digs :", digs)

    for d in range(len(digs)) :
        i, j = digs[d-1], digs[-d]
        # print(i, ":", j)
        if i != j :
            return False
    return True

if __name__ == '__main__':
    print(is_palindrome(1221))