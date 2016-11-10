class Kls(object):

    def __init__(self, data):
        self.data = data

    def printd(self):
        print self.data

    @staticmethod
    def smethod(*arg):
        print "static", arg

    @classmethod
    def cmethod(*arg):
        print "class", arg


ik = Kls('zzz')
ik.printd()
ik.smethod(['cbb', 'zyc'])

ik.cmethod(['cbb', 'zyc'])
