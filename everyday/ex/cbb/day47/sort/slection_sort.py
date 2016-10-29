# -*- coding: utf-8 -*-
'''
选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理大致是将后面的元素最小元素一个个取出然后按顺序放置。

在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。
'''

def selection_sort(list):
    n = len(list)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if list[j] < list[min]:
                min = j
                list[min],list[i] = list[i],list[min]
    return list

zjw = [1,3,2,10,4,5]
print selection_sort(zjw)