from functools import total_ordering
@total_ordering
class word(str):
    def __new__(cls, word):
        if ' ' in word:
            print "Value contains spaces. Truncating to first space"
            word = word[:word.index(' ')]
        return str.__new__(cls,word

    def __pos__(self):
        return 

zz1 = word('ao')
zz2 = word('bar')


print dir(zz1)