class A():
    def __init__(self):
        print "call __init__"
        self.a = 1

    def __new__(self):
        print "call __new__"

    def __del__(self):
        print "call __del__"

    def __str__(self):
        print "call __str__"
        return "class A str"

    def __repr__(self):
        print "call __repr__"
        return "class A repr"

    def __unicode__(self):
        print "call __unicode__"
        return "class A unicode"

    def __nozero__(self):
        print "call __nozero__"
        return 1

    def __len__(self):
        print "call __len__"
        return 1

    def __call__(self, *args):
        print "call __call__"
a = A()
print a
repr(a)
unicode(a)
print bool(a)
print len(a)
print callable(a)