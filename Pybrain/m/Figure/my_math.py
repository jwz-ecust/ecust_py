# -*- coding: utf-8 -*-
'''
某数学考试
填空题 8道， 答对一道得4分，未答对0分
问答题 6道， 答对一道得7分，未答对0分
考试人数400人
问：
  至少有多少人的总分相同?
'''

score = []
for i in range(8+1):
    for j in range(6+1):
        score.append(i*4+j*7)

score = set(score)
print len(score)
least = 400./len(score)
print least
