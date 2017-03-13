# -*- coding: utf-8 -*-

IND = 'ON'

def checkind():
    return (IND=='ON')

class kls(object):
    def __init__(self,data):
        self.data = data

    def do_rest(self):
        if checkind():
            print "reset done for:", self.data

    def set_db(self):
        if checkind():
            self.db = "New db connection"
        print "DB connection made for:", self.data

ik1 = kls(12)
ik1.do_rest()
ik1.set_db()

