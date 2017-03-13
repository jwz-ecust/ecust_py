from decimal import Decimal

class Fees(object):
    def __init__(self):
        self._fee = None

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self,value):
        if isinstance(value,str):
            self._fee = Decimal(value)
        elif isinstance(value,Decimal):
            self._fee = value

    @fee.deleter
    def fee(self):
        del self._fee


f = Fees()
f.fee = "111"
print f.fee
print dir(f)

del f.fee
print f.fee