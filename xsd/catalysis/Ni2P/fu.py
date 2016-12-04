class person(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


bb = person('Bob Smith')
print bb.name
bb.name = "zhangjiawei"
print bb.name
del bb.name
print hasattr(bb, 'name')


sue = person("Sue Jones")
print sue.name
