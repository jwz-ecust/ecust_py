# -*- coding: utf-8 -*-
'''
deque其实是 double-ended queue 的缩写
翻译过来就是双端队列
它最大的好处就是实现了从队列 头部快速增加和取出对象: .popleft(), .appendleft()
list对象的这两种用法的时间复杂度是 O(n) ，也就是说随着元素数量的增加耗时呈 线性上升。
而使用deque对象则是 O(1) 的复杂度，所以当你的代码有这样的需求的时候， 一定要记得使用deque。
'''

import sys
import time
from collections import deque

d = deque()
d.append('1')
d.append('2')
d.append('3')
print len(d),d
dd = deque(range(5))
d.popleft()
d.pop()
print d
d.extendleft([111])
d.extend([6,7,8])
print d


fancy_loading = deque('>--------------------')

while True:
    print '\r%s' % ''.join(fancy_loading),
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)



