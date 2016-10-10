class Fib(object):
    def __init__(self,max):
        self.max = max
        self.a = 0
        self.b = 1

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

fib = Fib(100)
res = []
for i in range(12):
    res.append(fib.__next__())

print res, '\n',len(res)