class zjw:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def aa(self):
        return self.a

    @aa.setter
    def aa(self, i):
        if isinstance(i, (int, str)):
            self.a = i
        else:
            raise ValueError

    @property
    def bb(self):
        return self.b

    @property
    def cc(self):
        return self.c


cc = zjw(1,2,3)

print(cc.aa)
cc.aa = 10
print(cc.aa)
cc.aa = 'zjw'
print(cc.aa)
