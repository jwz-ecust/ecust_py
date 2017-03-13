class Root(object):
    def __init__(self):
        print "this is Root"

class B(Root):
    def __init__(self):
        print "enter B"
        Root.__init__(self)
        # super(B,self).__init__()
        print "leave B"

class C(Root):
    def __init__(self):
        print "enter C"
        Root.__init__(self)
        # super(C,self).__init__()
        print "leave C"

class D(B,C):
    pass


d = D()



'''
enter B
enter C
this is Root
leave C
leave B


This is called the MRO.
'''