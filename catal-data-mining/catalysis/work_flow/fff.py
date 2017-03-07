class zjw(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hh(self):
        print "fuck"

    def cc(self):
        self.hh()


zz = zjw('a', 'b')
zz.cc()
