# -*- coding: utf-8 -*-
import operator

"""
doc_description:
    itemgetter(item, ...) --> itemgetter object

    Return a callable object that fetches the given item(s) from its operand.
    After f = itemgetter(2), the call f(r) returns r[2]
    After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
"""

student = [
    {'name': 'fang', 'age': 24},
    {'name': 'job', 'age': 20},
    {'name': 'zen', 'age': 40}
]

# 对字典的操作
# b = operator.itemgetter('name', 'age')
# for i in student:
#     print b(i)


# 与sorted函数一块使用
# studict = [{'jack': 89}, {'rose': 40}, {'bils': 70}, {'zend': 30}]
# a1 = sorted(studict)
# print "sorting by a1:", '\n', a1
# # 按照key来排序
# a2 = sorted(studict, key=lambda x: x.keys())
# print "sorting by a2:", '\n', a2
# # 按照value来排序
# a3 = sorted(studict, key=lambda x: x.keys())
# print "sorting by a3:", '\n', a3
#
# # 当操作对象是列表时，可以把key指定的lambda函数换成 operator.itemgetter(index)
#
student = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
#
# # 通过studict的第三个域排序
a4 = sorted(student, key=lambda x: x[2])
print "sorting by a4:", '\n', a4
#
# # operator.itemgetter 的形式通过studict的第三个域排序
a5 = sorted(student, key=operator.itemgetter(2))
print "sorting by a5:", '\n', a5
#
# # 根据第二个域和第三个域进行排序
a6 = sorted(student, key=operator.itemgetter(1, 2))
print "sorting by a6", '\n', a6