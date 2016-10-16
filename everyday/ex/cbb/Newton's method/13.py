# -*- coding: utf-8 -*-

# A simple Newton's method

def dx(f,x):
    return abs(0-f(x))

def newtons_method(f,df,x0,e):
    delta = dx(f, x0)
    n=1
    while delta > e:
       n +=1
       x0 = x0*1.0 - f(x0)/df(x0)
       delta = dx(f,x0)
    print 'Root is at: ',x0
    print 'f(x) at root is: ', f(x0)
    print 'step: ',n

def f(x):
    return 6*x**5-5*x**4-4*x**3+3*x**2
def df(x):
    return 30*x**4-20*x**3-12*x**2+ 6*x


newtons_method(f,df,200,1e-5)