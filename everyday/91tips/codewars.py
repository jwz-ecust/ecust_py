#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/17

from itertools import permutations
a = raw_input("please input a number")
number_list = list(a)
number = []
for i in permutations(number_list):
    number.append(int(''.join(i)))
number.sort()
number = list(set(number))
index = number.index(int(a))
if index != len(number)-1:
    print number[index+1]
else:
    print "all elements are the same! or the input number has no next-bigger"
