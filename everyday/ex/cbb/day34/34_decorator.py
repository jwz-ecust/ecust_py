# -*- coding: utf-8 -*-

'''
decoration example
===============================================
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run
=================================================
'''

from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)  # this is used to keep the function name as you want
    def wrapTheFunction():
        print "I am doing some boring work before understanding"
        a_func()
        print "I have done with func"
    return wrapTheFunction


@a_new_decorator
def a_func_requiring_decoration():
    print "I am the function which needs some decoration to remove my foul sme\
    ll"


a_func_requiring_decoration()
print a_func_requiring_decoration.__name__
