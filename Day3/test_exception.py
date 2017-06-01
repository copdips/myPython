def sqrt(x):
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20 :
            print("i", i)
            print("guess before:",guess)

            guess = (guess + x / guess) / 2.0
            print("guess after:",guess)

            i += 1
        return guess
    except ZeroDivisionError as zd:
        print("except ZeroDivisionError : ", zd)

print(sqrt(-1))


