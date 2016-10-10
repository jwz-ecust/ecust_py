# -*- coding: utf-8 -*-
from functools import wraps

'''
装饰器在日志中的应用
'''

def logit(func):
    @wraps(func)
    def with_logging(*args,**kwargs):
        print func.__name__ + 'was called'
        return func(*args,**kwargs)
    return with_logging

@logit
def addition_func(x):
    """
    do some math
    """
    return x+x

print addition_func(10)