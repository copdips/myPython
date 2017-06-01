class Fraction:
    """ class Fraction """
    def __init__(self, N, D):
        self.num = N
        self.den = D

    def __str__(self):
        res = str(self.num) + "/" + str(self.den)
        return res

    def __repr__(self):
        # return self.__str__()
        res = str(self.num) + "/" + str(self.den)
        return res

    def __mul__(self, autre):
        return Fraction(self.num * autre.num , self.den * autre.den)

    def __add__(self, autre):
        return Fraction(self.num * autre.den + autre.num * self.den , self.den * autre.den)

    def __sub__(self, autre):
        return Fraction(self.num * autre.den - autre.num * self.den , self.den * autre.den)

    def __truediv__(self, autre):
        return Fraction(self.num * autre.den , self.den * autre.num)

    def coucou(self):
        """ coucou """
        return "coucou " + str(self.num)

    def coucou2(self):
        """ coucou2 """
        return "coucou2 " + str(self.num)

f1 = Fraction(3, 4)

print(type(f1))
print(dir(f1))
print(f1.num)
print(f1)
print(f1.coucou())

f2 = Fraction(1, 4)


print(f1 * f2)

print(f1 + f2)

print(f1 - f2)

print(f1 / f2)


