class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b =b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            end = n.stop
            a,b = 1,1
            L = []
            for x in range(end):
                if x>=start:
                    L.append(a)
                a,b = b,a+b
            return L
    @property
    def name(self):
        return "chenbeibei"

    def __getattr__(self, attr):
        if attr == 'name':
            return "zhangjiawei"


a = Fib()

print a[10:101]
print a.name