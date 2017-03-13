class zjw(object):

    def __init__(self):
        self.name = 'zhangjiawei'

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "hello, I am {}".format(self.name)


foo = zjw()

print hasattr(foo,'setName')
print getattr(foo,'name','NA')
setattr(foo,'age',20)

print foo.__dict__