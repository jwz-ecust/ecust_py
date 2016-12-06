class Reactangle:
    def __init__(self):
        self.width = 0
        self.hight = 0
    def __setattr__(self, name, value):
        if name == "size":
            self.width, self.hight = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        if name == "size":
            return self.width, self.hight
        else:
            raise AttributeError


# zjw = Reactangle()
# zjw.size = [10, 11]
# print zjw.size




class power(object):
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    @property
    def square(self):
        return self._square **2
    @square.setter
    def square(self, value):
        self._square = value

    @property
    def cube(self):
        return self._cube**3
    @cube.setter
    def cube(self, value):
        self._cube = value


X = power(2, 3)
print X.square, X.cube
X.cube = 111
print X.cube
