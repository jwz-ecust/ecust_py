# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
# f1,f2,f3 = count()
# print f1(),f2(),f3()
#
# print f1.__closure__[0].cell_contents
#
#
# def cout2():
#     fs = []
#     for j in range(1,4):
#         def ff(m=j):
#             return m*m
#         fs.append(ff)
#     return fs
#
# ff1,ff2,ff3 = cout2()
#
# print ff1.__closure__

f1, f2, f3 =  [lambda j=i:j*j for i in range(1,4)]
print i
print f1(), f2() ,f3()
i = 5
print f1(), f2() ,f3()