import heapq
'''
Example:
portfolio = [
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'APPLE','shares':50,'price':543.22},
    {'name':'FACEBOOK','shares':200,'price':21.9},
    {'name':'HP','shares':35,'price':31.75},
    {'name':'YAHOO','shares':45,'price':16.35},
    {'name':'ACME','shares':75,'price':115.65},
]
print heapq.nlargest(4,portfolio,key=lambda s:s['price'])
print heapq.nsmallest(4,portfolio,key=lambda s:s['name'])
'''

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foor'),1)
q.push(Item('z'),5)
q.push(Item('j'),2)
q.push(Item('w'),4)
q.push(Item('cbb'),3)
q.push(Item('zyc'),1)
print q._queue