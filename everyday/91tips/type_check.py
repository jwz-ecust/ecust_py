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
        raise NotImplementedError("not support operation")

    def __str__(self):
        return str(self._val)

    def __repr__(self):
        return "Integer(%s)" % self._val


n = UserInt()
print n

m = UserInt(2)
print m

print m + n

print isinstance(type(n), types.IntType)
