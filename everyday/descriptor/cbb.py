'''
a.x 查找的顺序:
[查找 a.__dict__['x']] ==> [查找 type(a).__dict__['x']] ==> [查找 type(a)的父类, 不包括(metaclass)]
'''


class Ts(object):
    def __init__(self):
        self.a = 10090238409382
        self.b = 200


class Ts2(object):
    def __init__(self):
        self.a = 1
        self.b = 0.1

    def __set__(self, isinstance, value):
        print "__set__", isinstance, value
        return self

    def __get__(self, isinstance, owner):
        print "__get__", isinstance, owner
        return self


class TT1(object):
    def __init__(self):
        self.x = 1000
        self.y = 100
        self.z = 10

    x1 = Ts()
    y1 = 10
    a = 1
    x2 = Ts2()


if __name__ == '__main__':
    t = TT1()
    print t.__dict__
    print type(t)
    print type(t).__dict__
    print type(type(t))
    print t.x1.a
    print t.x2
    print t.y
    print t.a
