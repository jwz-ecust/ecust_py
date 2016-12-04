class listinstance:

    def __str__(self):
        return "<Instance of %s, address %s:\n%s>" % (self.__class__.__name__, id(self), self.__attrnames())

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (attr, self.__dict__[attr])
        return result


class Super:

    def __init__(self):
        self.data1 = "spam"

    def ham(self):
        pass


class Sub(Super, listinstance):

    def __init__(self):
        Super.__init__(self)
        self.data2 = "eggs"
        self.data3 = 42

    def spam(self):
        pass


X = Sub()
print X
