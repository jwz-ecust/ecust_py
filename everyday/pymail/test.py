# import collections
#
#
# class LoggingDict(object):
#     pass
#
#
# class LoggingOD(LoggingDict, collections.OrderedDict):
#     pass
#
#
# print LoggingOD.__base__
# print LoggingOD.__mro__


class A(object):
    pass


class B(A):
    pass


class C(B,A):
    pass


class D(C, B, A):
    pass


print D.__base__
print D.__mro__
