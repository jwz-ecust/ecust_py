#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/16
import itertools


def check(a, b):
    for i in zip(a, b):
        if i in [('a', 'x'), ('c', 'x'), ('c', 'z')]:
            return
    else:
        return a, b

team_1 = ['a', 'b', 'c']
team_2 = ['x', 'y', 'z']
for i in itertools.permutations(team_1, 3):
    print check(i, team_2)
