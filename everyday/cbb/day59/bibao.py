# def count():
#     fs = []
#     for i in range(1,4):
#         def f(m=i):
#             return m*m
#         fs.append(f)
#     return fs
#
#
# f1,f2,f3 = count()
# print f1(),f2(),f3()




def count():
    fs = []
    for i in range(1,4):
        f = (lambda x: x*x)(i)
        fs.append(f)
    return fs

f1,f2,f3 = count()
print f1()