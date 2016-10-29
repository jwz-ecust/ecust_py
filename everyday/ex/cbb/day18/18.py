# -*- coding: utf-8 -*-
'''
Counter
统计不同元素的个数，将元素与其个数对应，构造一个字典。
'''


with open('test.txt', 'r') as f:
    from collections import Counter
    c = Counter()
    for line in f:
        words = line.split()
        print words
        c += Counter(words)

    for words in c.most_common():
        print words
