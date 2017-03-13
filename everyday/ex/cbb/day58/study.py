# -*- coding: utf-8 -*-
Study_content = ['__repr__','__str__','__getattribute__','__format__']

# __repr__ and __str__
#对于一个对象,python有两种字符串表示方法.
#这些都是和内置函数 __repr__(),__str__(),__print__()以及string.format()方法紧密结合

   #str()方法表示的对象通常是适用于人理解的,由对象的__str__()方法创建
   #repr()方法表示的对象通常是适用于解释器解释的,可能是完整的Python表达式来重建对象. 对于许多类型,这个函数试图返回一个字符串,将该字符串传递给eval()会重新生成对象
   #print()函数会使用str()准备对象用于打印

class Card(object):
    insure = False
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()
    def __repr__(self):
        return "{__class__.__name__!s}(surt={suit!r},rank={rank!r})".format(__class__=self.__class__,**self.__dict__)
    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)

class NumberCard(Card):
    def _points(self):
        return int(self.rank),int(self.rank)

x = NumberCard('2','zjw')

print str(x),'\n',repr(x),'\n',x

print "#"*50


# NumberCard(surt='zjw',rank='2')
