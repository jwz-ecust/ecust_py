import base


@base.export
class B(object):
    pass


@base.export
def func_b():
    print "func_b"
