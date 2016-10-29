#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/28

import  numpy as np
from scipy.optimize import leastsq
import pylab as pl


def func(x, p):
    A, k, theta = p
    return A*np.exp(2*np.pi*k*x + theta)


def residuals(p, y, x):
    return y - func(x, p)


np.random.seed(1)

x = np.arange(1, 17, 1)
y = np.arange(1, 17, 1)
y = y + 5*np.random.rand(len(y))

# first
z1 = np.polyfit(x, y, 3)
p1 = np.poly1d(z1)

# second
z2 = np.polyfit(x, y, 6)
p2 = np.poly1d(z2)

# third
z3 = np.polyfit(x, y, 1)
p3 = np.poly1d(z3)

#fourth
p0 = [7, 0.2, 0]
plsq = leastsq(residuals, p0, args=(x, y))


pl.plot(x, y, 'bo', label="origin line")
pl.plot(x, p1(x), 'gv--', label="first: poly fitting 3")
pl.plot(x, p2(x), 'r*', label="second: poly fitting 6")
pl.plot(x, p3(x), 'y-', label="third: poly fitting 1")
pl.plot(x, func(x, plsq[0]), 'k:', label="fourth: poly fitting by scipy_leastsq")

pl.axis([0, 18, 0, 18])
pl.legend(loc='best')
pl.show()



