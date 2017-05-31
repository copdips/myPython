import math

def f(a, b, c=10) :
    """ f doc """
    print(a**b+c)

f(2, 31, 2)
# f(a=2, 31, 2)
# f(2, c=31, a=2)
f(2, c=31, b=2)
f(c=3, a=31, b=2)
f(3, 2)


def mean1(aList):
    """ calculate average of a number list """
    print("mean1", aList)
    # res = sum(i for i in aList) / len(aList)
    res = sum(aList)/len(aList) if aList !=[] else None
    print(res)

mean1([1,2,3,4,5])





def mean2(*a):
    """ calculate average of the arguments number """
    print("mean2", a)
    res = sum(a) / len(a)
    print(type(a))
    print(res)

def mean3(*a):
    """ calculate average of the arguments number """
    print("mean3", a)
    b = list( bb for bb in a if type(bb) in {int,float})
    res = sum(b) / len(b)
    print(type(b))
    print(res)

def mean4(a,b,c):
    """ équation """
    print("mean4", a, b, c)
    delta = b**2-4*a*c
    if delta < 0 :
        res=(0,"Pas de solution")
    elif int(delta) == 0 :
        x = -b/2/a
        res=(1, x)
    elif delta > 0 :
        x = {(-b+delta**0.5)/2/a, (-b-delta**0.5)/2/a}
        res=(2, x)
    else :
        res = None
    print(res)

mean2(1, 2)
mean2(1, 2, 3)

mean3(1,2,3)
mean3(1,"sdfsdf","sdfsdfsdff",2,3,4)
mean3(1,"sdfsdf","sdfsdfsdff",2,3,4.00)

mean4(4,1,1)
mean4(4,4,1)
mean4(4,6,1)
