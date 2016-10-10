# -*- coding: utf-8 -*-

import glob
from collections import Counter

def mostImportantWord(filePath):
    for file in glob.glob(filePath+'*.txt'):
        calcTimes(file)

def calcTimes(fileName):
    cc = Counter()
    with open(fileName) as file:
        str = file.read()
        words = str.split('\n')
        for i in words:
            cc[i] = cc[i] + 1
        maxInDict(cc)

def maxInDict(dict):
    max = 0
    for key, value in dict.items():
        if value > max:
            max = value
            goal = key
    print goal + "and its time's " + str(max)

mostImportantWord('diaries/')


