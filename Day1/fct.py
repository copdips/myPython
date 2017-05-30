def f(a, b, c=10) :
    """ f doc """
    print(a**b+c)

f(2, 31, 2)
# f(a=2, 31, 2)
# f(2, c=31, a=2)
f(2, c=31, b=2)
f(c=3, a=31, b=2)
f(3, 2)

print("mean1")
def mean1(aList):
    """ calculate average of a number list """
    # res = sum(i for i in aList) / len(aList)
    res = sum(aList)/len(aList) if aList !=[] else None
    print(res)

mean1([1,2,3,4,5])


print("mean2")


def mean2(*a):
    """ calculate average of the arguments number """
    res = sum(a) / len(a)
    print(type(a))
    print(res)


mean2(1, 2)
mean2(1, 2, 3)
