#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/17


def plus(n):
    if n == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1)) + plus(n - 1)


print plus(20)
