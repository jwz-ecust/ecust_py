# -*- coding:utf-8 -*-
'''
依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple),
提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass。

'''

class Person(object):
    def __new__(cls, name, age):
        print "__new__ called"
        return super(Person,cls).__new__(cls,name,age)

    def __init__(self, name, age):
        print "__init__ was called"
        self.name = name
        self.age = age

    def __str__(self):
        return "<Person: %s(%s)>" %(self.name,self.age)



class PostieInter_init(int):
    def __init__(self,value):
        super(PostieInter_init,self).__init__(self,float(value))

j = PostieInter_init(-11)
print j

class PostiveInteger_new(float):
    def __new__(cls,value):
        return super(PostiveInteger_new, cls).__new__(cls, float(value))

i = PostiveInteger_new(-3)
print i



