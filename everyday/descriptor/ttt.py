class ff(object):

    def __init__(self):
        self.x = 1.0

    def __get__(self, isinstance, owner):
        # print "getting", self.x
        return self.x

    def __set__(self, isinstance, value):
        self.x = value


class zjw(object):

    def __init__(self):
        self.x = 10
    x = ff()


z = zjw()
print z.x
z.x = 1010100101
print z.x
