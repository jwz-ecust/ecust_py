# -*- coding: utf-8 -*-
# 属性描述符


class Descripter(object):

    def __get__(self, isinstance, owner):
        print self, isinstance, owner
        # return self.owner

    def __set__(self, isinstance, value):
        print self, isinstance, value
        # self.instance = value


class testclass(object):
    des = Descripter()

    def __getattribute__(self, name):
        print "before __getattribute__"
        return super(testclass, self).__getattribute__(name)
        print "after __getattribute__"

    def __setattr__(self, name, value):
        print "before __setattr__"
        super(testclass, self).__setattr__(name, value)


test1 = testclass()
test2 = testclass()

test1.Des = "hehehehe"
test2.des
