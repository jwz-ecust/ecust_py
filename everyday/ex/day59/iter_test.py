from __future__ import print_function


# class number:
#
#     def __init__(self, data):
#         self.data = data
#
#     def __sub__(self, other):
#         print "starting subbing"
#         return number(self.data - other)
#
#     def __str__(self):
#         print "num ==> str"
#         return str(self.data)
#
#
# # a = number(10)
# # b = 2
# # c = a - 2
# # print c
#
#
# class square:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         self.a, self.b = self.b, self.b + self.a
#         return self.a
#
#
# # t = 0
# # a = square(1, 1)
# # for i in a:
# #     if t < 1000:
# #         print i
# #         t += 1
#
#
# class SkipObject:
#
#     def __init__(self, wrapped):
#         self.wrapped = wrapped
#         self.offset = 0
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.offset >= len(self.wrapped):
#             raise StopIteration
#         else:
#             item = self.wrapped[self.offset]
#             self.offset += 2
#             return item

# a = "zhangjiawei"
# zjw = SkipObject(a)
#
# for i in zjw:
#     b = SkipObject(a)
#     for j in b:
#         print i + j


class Iters:

    def __init__(self, value):
        self.data = value

    # def __getitem__(self, i):
    #     print ('get[%s]: ' % i, end=' ')
    #     return self.data[i]
    #
    # def __iter__(self):
    #     print ("iter==>", end=' ')
    #     self.ix = 0
    #     return self
    #
    # def next(self):
    #     print ("next:", end=' ')
    #     if self.ix == len(self.data):
    #         raise StopIteration
    #     item = self[self.ix]
    #     self.ix += 1
    #     return item

    def __contains__(self, x):
        print ("contains:", end=' ')
        return x in self.data


# X = Iters([1, 2, 3, 4, 5])
#
# print (3 in X)
#
# print (map(bin, X))
#
# for i in X:
#     print (i, end='$\n')


class zjw:

    def __setattr__(self, attr, value):
        if attr in self.__dict__.keys():
            print ("not allowed")
            raise AttributeError
        else:
            self.__dict__[attr] = value
a = zjw()
a.name = 'zjw'
print (a.name)
