#!/usr/bin/env python
# -*- codin: utf-8

__author__ = 'jwzhang@ecust'


def readFile(filepath):
    file = open(filepath, 'r')
    words = []
    for word in file.readlines():
        words.append(word.strip('\n'))
    return words


def check(testWord):
    realWords = readFile('filtered_words.txt')
    for i in realWords:
        if i == testWord:
            print "freedom"
            return
        else:
            print "Human Rights"
            return


if __name__ == '__main__':
    check('sss')
    check("牛逼")
