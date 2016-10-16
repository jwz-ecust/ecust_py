#!/usr/env/bin pyton
# date: 2016-10-16
# time: 16:51:30

"""
this is a script uesed for factor calculation
output: 100=2*2*5*5
"""


def factor(num):
    t = num
    prime_list = [i for i in range(2,t/2+1) if is_prime(i)]
    res = []
    for i in prime_list:
        while True:
            if t % i == 0:
                t = t/i
                res.append(i)
            else:
                break
        if is_prime(t):
            res.append(t)
            break
    print "{}={}".format(str(num),'*'.join([str(i) for i in res]))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n/2+1):
        if n%i == 0:
            return False
    else:
        return n


factor(2046)
# output: 2046=2*3*11*31
