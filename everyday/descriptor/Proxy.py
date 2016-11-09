# -*- coding: utf-8 -*-


class Proxy(object):

    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        """
        __setattr__() 和 __delattr__() 需要额外的魔法来区分代理实例和被代理实例 _obj 的属性。
        一个通常的约定是只代理那些不以下划线 _ 开头的属性(代理类只暴露被代理类的公共属性)。
        """
        if key.startswith("_"):
            print "in super"
            print self.__class__
            super(Proxy, self).__setattr__(key, value)
            print self.__class__
        else:
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super(Proxy, self).__delattr__(item)
        else:
            delattr(self._obj, item)


class Spam(object):

    def __init__(self, x):
        self.x = x

    def bar(self, y):
        return 'Spam.bar', self.x, y


s = Spam(2)
p = Proxy(s)
print p.x
p.x = 1000
print p.x
del p.x

p._x = 5
print p._x
