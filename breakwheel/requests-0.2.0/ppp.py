# -*- coding: utf-8 -*-
'''
描述符  Python新式类的关键之一
    为对象属性提供强大的API, 你可以认为描述符是表示对象属性的一个代理。当需要属性时， 可以
    根据你遇到的情况，通过描述符进行访问。
'''

# 使用类方法创建描述符
# 奖某种特殊类型的类的实例指派给另一个类的属性。这种特殊类就是实现了  __get__, __set__, __delete

#  __get__(self, object, type)  用于得到一个属性的值
# __set__(self, obj, val)   用于为一个属性赋值
# __delete__(self, obj)    删除某个属性时调用，很少用


"""
当只有__set__ ==> 方法描述符
当有 __set__ 和 __get__ ==> 数据描述符
"""

# 数据类描述符
class Descriptor(object):
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print "访问属性"
        return self.value

    # def __set__(self, instance, value):
    #     print "设置属性值"

        self.value = value


# 定义一个调用数据描述符的类
# class myclass(object):
#     desc = Descriptor(5)


class mm(object):
    desc = Descriptor(5)
    def __init__(self, desc):
        self.desc = desc

z = mm(1)
# print z.desc
#
# print z.__dict__
# print mm.__dict__





class ppp(object):
    def __init__(self):
        self._name = " "

    def fget(self):
        print "Getting: %s" %self._name
        return self._name

    def fset(self, value):
        if isinstance(value, str):
            print "Setting: %s" %value
            self._name = value
        else:
            print "Setting Error"

    def fdel(self):
        print "Deleting: %s" %self._name
        del self._name

    name = property(fget, fset, fdel, "I'm the property!")


p = ppp()
p.name = "zhangjiawei"
p.name = 1
