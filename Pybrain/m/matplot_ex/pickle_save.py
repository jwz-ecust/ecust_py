#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/27
import pickle
import numpy.random as rd

x = rd.randn(1000)
y = rd.randn(1000)
z = rd.randn(1000)
u = rd.randn(1000)
pickle.dump([x, y, z, u], open('ppp.p', 'w'))
