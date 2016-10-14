#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/14

# from collections import namedtuple
#
# def enum(*posarg, **keysarg):
#     #   返回一个类, type 可以构造类
#     return type("Enum", (object,),
#                 dict(zip(posarg, xrange(len(posarg))), **keysarg))
#
#
# Seasons = enum("Spring","Summer", "Autumn", winter=1)
# print Seasons
# print type(Seasons)
# print Seasons.__dict__
#
#
# Season = namedtuple("Season", "spring summer autumn winter")._make(range(4))
# print Season
# Season._replace(spring=2)
# print Season



from flufl.enum import Enum


class zjw_season(Enum):
    Spring = "spring"
    Summer = 2
    Autumn = 3
    Winter = 4

zjw_season = Enum("zjw_season","Spring Summer Autumn Winter")

print zjw_season.__dict__
print zjw_season.Summer.value
