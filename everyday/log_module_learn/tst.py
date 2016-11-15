class base(object):

    def __init__(self, path):
        pass


class A(object):

    def __init__(self, path):
        self.load()

    def load(self):
        setattr(self, 'b', 1)
        self.a = 1

    def __eq__(self, other):
        if self.__dict__ == other.__dict__:
            return True
        else:
            return False

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True


class B(base):

    def __init__(self, path):
        super(B, self).__init__(path)
        self.load()

    def load(self):
        setattr(self, 'b', 1)

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True

path1 = "/Users/zhangjiawei/Code/zjw/xsd/VASPy-master/vaspy/INCAR"
path2 = "/Users/zhangjiawei/Code/zjw/xsd/VASPy-master/vaspy/INCAR_uspex"

a = A(path1)
b = A(path2)
print a != b

a1 = B(path1)
b1 = B(path2)
print a1 != b1
