# -*- coding: utf-8 -*-

#装饰器@staticmethod和@classmethod的区别
from docopt import printable_usage


class A(object):
    def foo(self,x):
        print "excuting foo {} {}".format(self,x)

    @classmethod
    def class_foo(cls,x):
        print "excuting class_foo {} {}".format(cls,x)

    @staticmethod
    def static_foo(x):
        print "excuting static_foo {}".format(x)

a = A()
a.foo('zhangjiawei1')        # 对象实体调用方法，对象实体a被隐藏地传递给了第一个参数。
a.class_foo('zhangjiawei2')  #用classmethods装饰，隐藏地传递给第一个参数地是对象实体的类(class A),而不是self
a.static_foo('zhangjiawei3') #用staticmethods来装饰的话，不管传递给第一个参数的self是对象or实体，他们的表现都是一样的
A.class_foo('zhangjiawei')   #实际上希望用类来调用class方法，而不是通过实例来调用这个类方法


'''
excuting foo <__main__.A object at 0x00000000029DBB00> zhangjiawei1
excuting class_foo <class '__main__.A'> zhangjiawei2
excuting static_foo zhangjiawei3
excuting class_foo <class '__main__.A'> zhangjiawei
'''
print a.foo
print a.class_foo, 'is equal to', A.class_foo
print a.static_foo