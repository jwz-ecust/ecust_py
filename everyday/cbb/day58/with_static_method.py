# -*- coding: utf-8 -*-

class kls(object):
    __IND__ = "ON"
    def __init__(self,data):
        self.data = data

    @staticmethod
    def checkind(x):
        return (x == "ON")

    def do_reset(self):
        if self.checkind():
            return

    def set_db(self):
        if self.checkind():
            self.db = "New db connection"
        return

    @classmethod
    def newcheck(cls,y):
        return "this is class method, {} {}".format(y,cls.__IND__)

zjw = kls(11)
print zjw.checkind("OFF")
print zjw.newcheck('zjw')