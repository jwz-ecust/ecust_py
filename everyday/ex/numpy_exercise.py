#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/15

import numpy as np

person_type = np.dtype({
    "names": ["name", "age", "weight"],
    "formats": ['S32', 'i', 'f']})

a = np.array([("Zhangjiawei", 26, "84.0"), ("chenbeibei", 26, 65.2)], dtype=persontype)
print a, '\n', a.dtype,  type(a[:]['name']), a[:]['age']
# a.tofile("test.bin")       #通过调用a.tofile方法,可以将构建的数据转换成二进制形式

z = np.arange(0, 100, 10)
print z
