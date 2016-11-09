# -*- coding: utf-8 -*-
# setattr()
# 说明：给object对象添加新的name(属性)和value(属性值)，通常在class中运用较多
'''
setattr(...)
    setattr(object, name, value)
    为object对象添加新的name属性和value属性值
    Set a named attribute on an object; setattr(x, 'y', v) is equivalent to
    ``x.y = v''.
'''


class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


student = Student('zjw', 26)
setattr(student, 'cbb', 27)
print student.__dict__
delattr(student, 'age')
print student.__dict__.has_key('age')
print student.__dict__
print getattr(student, 'name')
