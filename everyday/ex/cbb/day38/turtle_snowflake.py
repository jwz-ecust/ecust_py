# -×- coding: utf-8 -*-

from turtle import *
'''
分形
'''


def f(length, depth):
    if depth == 0:
        forward(length)
    else:
        f(length / 3, depth - 1)
        right(60)
        f(length / 3, depth - 1)
        left(120)
        f(length / 3, depth - 1)
        right(60)
        f(length / 3, depth - 1)


f(5000, 4)
