# -*- coding: utf-8 -*-
from collections import OrderedDict

items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)

regular_dict = dict(items)
ordered_dict = OrderedDict(items)

print 'Regular Dict:'
for k, v in regular_dict.items():
    print k, v

print 'Ordered Dict:'
for k, v in ordered_dict.items():
    print k, v
