# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # Created by jwz@ecust on 16/10/17
#
# from itertools import permutations
# a = raw_input("please input a number")
# number_list = list(a)
# number = []
# for i in permutations(number_list):
#     number.append(int(''.join(i)))
# number.sort()
# number = list(set(number))
# index = number.index(int(a))
# # if index != len(number)-1:
# #     print number[index+1]
# # else:
# #     print "all elements are the same! or the input number has no next-bigger"
#
# try:
#     print number[index+1]
# except:
#     print "all elements are the same or the input number has no next-bigger"
#
#
#
#


from fractions import Fraction


def fibonacci(n):
    a, b = 1, 2
    res = [1]
    i = 1
    while i < n:
        a, b = b, a + b
        res.append(a)
        i += 1
    else:
        return res


result = fibonacci(21)

sum_result = sum([Fraction(i[0], i[1]) for i in zip(result[1:], result[0:-1])])
print sum_result
