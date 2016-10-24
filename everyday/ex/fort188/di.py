#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is used to edit fort.188 file
# author: zjw-eucst
# date: 4:00pm 9-10-2016
import sys

with open('fort.188', 'r') as f1:
    content = f1.readlines()
    content[0] = ' 0\n'
    temp = [i for i in content[5].strip().split(' ') if i]
    temp[-1] = sys.argv[1]
    content[5] = ' ' + temp[0] + ' ' + temp[1] + ' ' * 4 + temp[2] + '\n'

with open('fort.188', 'w') as f2:
    f2.writelines(content)
