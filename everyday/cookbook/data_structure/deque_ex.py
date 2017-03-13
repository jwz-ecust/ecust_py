# -*- coding: utf-8 -*-
'''
保留历史记录
'''
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


lines = ['zjw', 'z', 'zz', 'j', 'jjj', 'zzzzz',
         'www', 'w', 'jb', 'jjj', 'jwz', 'ecust']
pattern = 'j'
history = 3

for i in search(lines, pattern, history):
    print i
