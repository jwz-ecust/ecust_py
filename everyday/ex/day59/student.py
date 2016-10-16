# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, score, a):
        self.s = score
        self._score = a

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError, "score must be an integer"
        if value < 0 or value > 100:
            raise ValueError, "score must be between 0 ~100"
        self._score = value


s = Student(55, 77)
s.score = 99
print s.score
print s.__dict__


class child(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        # 没有设置setter， 因此只有读取的属性， 无法设置age， age可以根据birth计算出
        return 2016 - self._birth + 1


zyc = child()
zyc.birth = 2016
# zyc.age = 0.5
print zyc.age
