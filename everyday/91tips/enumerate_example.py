#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/14
from flufl.enum import Enum


class zjw_season(Enum):
    Spring = "spring"
    Summer = 2
    Autumn = 3
    Winter = 4


zjw_season = Enum("zjw_season", "Spring Summer Autumn Winter")
print zjw_season.__dict__
print zjw_season.Summer.value
