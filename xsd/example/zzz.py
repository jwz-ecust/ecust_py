import os


class VasPy(object):

    def __init__(self, filename):
        if not os.path.exists(filename):
            raise ValueError("{} not exist.".format(filename))

        self.filename = filename


class InCar(VasPy):

    def __init__(self, filename='INCAR'):
        super(self.__class__, self).__init__(filename)
        self.filename = filename

    def __ne__(self, another):
        print self, another
        if self == another:
            return False
        else:
            return True

path1 = "/Users/zhangjiawei/Code/zjw/xsd/VASPy-master/vaspy/INCAR"
path2 = "/Users/zhangjiawei/Code/zjw/xsd/VASPy-master/vaspy/INCAR_uspex"
a1 = InCar(path1)
a2 = InCar(path2)
print a1 != a2
# False
