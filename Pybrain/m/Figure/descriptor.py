#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/27


class integer(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Nagative value not allowed")
        if not isinstance(value, int):
            raise ValueError("value must be int")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class movie(object):
    score = integer("score")
    ticket = integer("ticket")

a = movie()
a.score = 1
a.ticket = 100
a.score = 10000
