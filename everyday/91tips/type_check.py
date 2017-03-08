#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/14

import types


class UserInt(int):
    def __init__(self, val=0):
        self._val = val

    def __add__(self, val):
        if isinstance(val, UserInt):
            return UserInt(self._val + val._val)
        return self._val + val

    def __iadd__(self, val):
        # raise NotImplementedError("not support operation")
        # tt = self._val + val
        if isinstance(val, int):
            return UserInt(self._val + val)
        elif isinstance(val, UserInt):
            return UserInt(self._val, val._val)
        else:
            raise NotImplementedError("not support other type adding")

    def __str__(self):
        return "Integer(%s)" % str(self._val)

    def __repr__(self):
        return "Integer(%s)" % self._val


n = UserInt(11)
m = UserInt(212)
print n
n += 10
print n
n += m
print n
n += 1.0
