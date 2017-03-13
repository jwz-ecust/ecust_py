class A(object):
    def __init__(self):
        print "call __init__"
        self.value = 1

    def __new__(cls):
        print "call __new__"
        return super(A,cls).__new__(cls)

class zzz(A): pass
a = A()
print a.__new__(zzz)
print a.value