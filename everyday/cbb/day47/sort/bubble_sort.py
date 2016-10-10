# -*- coding: utf-8 -*-
'''
冒泡排序(Bubble Sort)是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
冒泡排序算法的运作如下：
    1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    3.针对所有的元素重复以上的步骤，除了最后一个。
    4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''
def bubble_sort(list):
    length = len(list)
    # 第一级排序
    for index in range(length):
        # 第二级排序
        for j in range(1,length-index)
            if list[j-1] > list[j]:
                list[j-1],list[j] = list[j],list[j-1]
    return list

def bubble_sort_flag(list):
    length = len(list)
    for index in range(length):
        flag = True  # 标志位
        for j in range(1,length-index):
            if list[j-1]>list[j]:
                list[j-1],list[j] = list[j],list[j-1]
                flag = False
        if flag:
            return list #没有发送交换，直接返回list
    return list
