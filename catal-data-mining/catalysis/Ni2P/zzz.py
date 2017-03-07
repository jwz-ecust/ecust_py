class Set:

    def __init__(self, value=[]):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return intersect(self, other)

    def __add__(self, other):
        if isinstance(other, int):
            self.data.append(other)
        elif isinstance(other, list):
            self.data.extend(other)
        return Set(self.data)

    def __or__(self, other):
        return self.union(self, other)

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return ','.join([str(_) for _ in self.data])

#
# x = Set([1, 3, 5, 6, 8])
# y = x + [11, 2, 31]
# print y


class newprops(object):

    def getage(self):
        return 40

    def setage(self, attr, value):
        print "set age: ", value
        self.attr = value

    age = property(getage, setage, None, None)


x = newprops()
print x.age
x.age = 10
x.zzz = 'zjjfal'
print x.zzz
