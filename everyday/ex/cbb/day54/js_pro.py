class access(object):
    def __init__(self):
        self._name = 'zhangjiawei'
        self._age = 20
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        if value>30:
            raise ValueError
        self._age = value
    @age.deleter
    def age(self):
        del self._name


zz = access()

zz.age=10
print zz.age