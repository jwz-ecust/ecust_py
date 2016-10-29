# -*- coding: utf-8 -*_


def calcWords(path):
    with open(path, 'r') as file:
        inputStr = file.read().split()
        return len(inputStr)


print calcWords('input.txt')
