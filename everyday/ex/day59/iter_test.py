class number:

    def __init__(self, data):
        self.data = data

    def __sub__(self, other):
        print "starting subbing"
        return number(self.data - other)

    def __str__(self):
        print "num ==> str"
        return str(self.data)


# a = number(10)
# b = 2
# c = a - 2
# print c


class square:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.b + self.a
        return self.a


# t = 0
# a = square(1, 1)
# for i in a:
#     if t < 1000:
#         print i
#         t += 1


class SkipObject:

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __iter__(self):
        return self

    def next(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

a = "zhangjiawei"
zjw = SkipObject(a)

for i in zjw:
    print i
