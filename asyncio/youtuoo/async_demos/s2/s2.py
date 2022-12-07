# 自己实现一个range
# for i in range(10):
#     print(i)


class MyRange:
    def __init__(self, total=0):
        self.total = total
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.total:
            x = self.count
            self.count += 1
            return x
        else:
            raise StopIteration


for i in MyRange(10):
    print(i)
