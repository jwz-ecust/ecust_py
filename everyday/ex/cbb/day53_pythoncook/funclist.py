# -*- coding: utf-8 -*-

class FunctionList:
    '''
    一个封装了一些加魔术方法: head,tail,init,last,drop and take
    '''
    def __init__(self,values = None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key]=value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self,value):
        self.values.append(value)

    def head(self):
        return self.values[0]

    def tail(self):
        return self.values[1:]

    def init(self):
        return self.values[:-1]

    def drop(self,n):
        return self.values[n:]

    def take(self,n):
        return self.values[:n]


zz  = FunctionList(values=[1,2,3])

print dir(zz)
print zz.__len__()