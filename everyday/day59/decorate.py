class classproperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, isinstance, owner):
        return self.func(owner)

    def __set__(self, isinstance, owner):
        return self


class Myclass(object):
    def __init__(self, val):
        self._data = val
        self.x = 3
        self.name = "test"

    @classproperty
    def name(cls):
        return cls.__name__

    @property
    def x(self):
        return self._data

    @x.setter
    def x(self, value):
        self._data = value

    @x.deleter
    def x(self):
        del self._data


s = Myclass(99)
print s.x
print s.name
print s.__dict__
