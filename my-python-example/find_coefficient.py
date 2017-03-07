# -*- coding: utf-8 -*-
import random
'''
Here is the question:
    存在一个多项式S(x)黑箱, 假设多项式的系数都是正整数(1-99之间), 如何通过最少的操作,
获取多项式的参数.

Method:
    取 x = 101
    求出 num = S(101)
    将 num 转化为 101 进制, 则对应的数字就是 多项式的各个系数.
'''


def ploy_generate(n):
    # n 代表多项式的项数
    # 生成一个多项式函数: an*x**n-1 + an-1*x**n-2 + ...+ a2*x + a1
    # 其中 ai 随机生成 的正整数
    coef_list = list()
    power_list = range(n)
    for i in range(n):
        coef_list.append(random.randint(1, 100))
    print coef_list
    return lambda x: sum([j[0] * x**j[1] for j in zip(coef_list, power_list)])


def N_system(num, N, n, zz_list=[]):
    # 讲数字转化为N进制的一个列表
    # N 代表进制
    # n 代表多项式的项数
    # 返回 多项式系数列表
    flag = True
    while flag:
        n = n - 1
        s, num = divmod(num, N**n)
        zz_list.append(s)
        if num == 0:
            flag = False
    return zz_list[::-1]


num = ploy_generate(10)(101)
print N_system(num, 101, 10)
