# -*- coding: utf-8 -*-
def f(n):
    if n == 1:
        return n
    else:
        return n + f(n-1)  # n 很大的时候会造成迭代过深，出错



def ff(n):
    if isinstance(n,int) and n>0:
        return int(n*(n+1)/2)

    
print ff(100)