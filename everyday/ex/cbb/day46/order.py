# -*- coding: utf-8 -*-
def order(sentence):
    list = sentence.split()
    ff = lambda word: int(filter(str.isdigit,word))  # filter 可以通过设置条件来过滤
    return sorted(list,key=ff,reverse=True)

print order("is2 Thi1s T4est 3a")



zjw = 'zja1wg3'
print filter(str.isdigit,zjw) # answer is '13'