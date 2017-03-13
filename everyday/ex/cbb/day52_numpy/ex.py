#! /usr/bin/python

import random
import sys

v = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]
     ]

def display(v,score):
    print '{0:4}{1:4}{2:4}{3:4}'.format(v[0][0],v[0][1],v[0][2],v[0][3])
    print '{0:4}{1:4}{2:4}{3:4}'.format(v[1][0],v[1][1],v[1][2],v[1][3])
    print '{0:4}{1:4}{2:4}{3:4}'.format(v[2][0],v[2][1],v[2][2],v[2][3])
    print '{0:4}{1:4}{2:4}{3:4}'.format(v[3][0],v[3][1],v[3][2],v[3][3]),'    Total score: ',score

def int(v):
    for i in range(4):
        v[i] = [random.choice([0,0,0,2,2,4]) for x in v[i]]

def align(vList,direction):
    for i in range(vList.count(0)):
        vList.remove(0)
