# -*- coding: utf-8 -*-
'''
##取值过程## ==> 伪代码
__getattribute__(propert) logic:

descriptor = find first descriptor in class and base's dict (property)
if descriptor:
    return descriptor.__get__(instance, instance.__class__)
else:
    if value in instance.__dict
        return value
    value = find first value in class bases's dict(property)
    if value is a function:
        return bonded function(value)
    else:
        return value
raise AttributeNotFundedException

##赋值过程##  ==> 伪代码
__setattr__(property, value) logic:

descriptor = find fist descriptor in class and bases's dict(property)
if descriptor:
    descriptor.__set__(instance, value)
else:
    instance.__dict__[property] = value
'''

# __getattribute__ and __getattr__


class tomorrow():

    def __init__(self, future, timeout):
        self.future = future
        self.timeout = timeout

    def __getattr(self, name):
        result = self._wait()
        return result.__getattribute__(name)

    def _wait(self):
        return self.future.result(self.timeout)


class ts(object):
    '''
    __getattribute__方法会优先调用
    且调用任何实例属性和方法都会调用__getattribute__,看的出来该方法其实就是-->属性调用。
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def method(self):
        pass

    def __getattr__(self, item):
        return item

    # def __getattribute__(self, item):
    #     return item + "***"


# t = ts(100, 20)
# print t.x
# m = t.y + t.x
# print m
# print t.y, t.name
# t.name = 'jb'
# print t.name


'''
Summary:
    1.__getattr__(self, name):找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。
    2.__getattribute__():在每次引用属性或方法名称时 Python 都调用它（特殊方法名称除外），不管属性或方法是否存在，也不管是否进行属性赋值等。
'''


#  __get__
class tss(object):
    '''
    object.__get__(self, instance, owner):如果class定义了它，则这个class就可以称为descriptor。
    owner是所有者的类，instance是访问descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None。
    descriptor的实例自己访问自己是不会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义。)
    '''

    def __get__(self, isinstance, owner):
        print "__get__", isinstance, owner
        return self

    def __call__(self, *args, **kwargs):
        print "__call__", self
        return self


class z(object):
    t = tss()


# zjw = tss()
# print zjw()
# print "*" * 30
#
# print z.t


# __getattr__ 常用于代理模式
class A(object):

    def foo(self):
        print 'sb'


class B(object):

    def __init__(self):
        self.a = A()

    def bar(self):
        pass

    def __getattr__(self, name):
        """这个方法在访问attribute不存在的时候被调用"""
        return getattr(self.a, name)


b = B()
b.bar()
b.foo()    # calls B.__getattr__(foo). and delegates to A.foo
