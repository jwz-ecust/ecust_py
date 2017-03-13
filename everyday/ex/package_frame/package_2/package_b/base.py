# -*- coding: utf-8 -*-
import sys

_packet_ = {}


# 它是一个装饰器, item是类, 或者函数
def export(item):
    # 获取item的模块对象
    module = sys.modules[item.__module__]
    # 由模块对象得到包对象
    package = sys.modules[module.__package__]
    # 吧item添加到包的__dict__里面
    package.__dict__[item.__name__] = item
    # 生成所有使用该解决方案的包的__all__变量, 并吧导出的item添加进去
    if not package.__name__ in _packet_:
        _packet_[package.__name__] = []
    _packet_[package.__name__].append(item.__name__)
    # 原封不动的吧item返回
    return item


# 它是哥函数, 在包__init__.py里用于获取__all__
def packet(name):
    if not name in _packet_:
        _packet_[name] = []
    return _packet_[name]
