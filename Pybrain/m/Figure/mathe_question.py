# -*- coding: utf-8 -*-

'''
先在黑板上写下一串数字：1，2，3，4....100
如果每次都擦去最前面6个数字
并在这串数字最后写上被擦去6个数字之和
得到一串新的数字
再做同样的操作
知道黑板上的数字不足6个
问：
1. 最后黑板上剩下的数字之和是多少？
2. 最后所写的哪个数是多少
'''

number = range(1, 101)

while len(number) > 6:
    part_sum = []
    for i in range(6):
        part_sum.append(number.pop(0))
    number.append(sum(part_sum))
else:
    print 'the sum of the remain is: ', sum(number)
    print 'the last number: ', number[-1]

