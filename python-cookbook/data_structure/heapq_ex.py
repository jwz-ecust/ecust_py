import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


q = PriorityQueue()
q.push(Item('fuck'), 1)
q.push(Item('dick'), 5)
q.push(Item('hole'), 3)
q.push(Item('ass'), 4)
q.push(Item("whole"), 1)


for i in range(5):
    print q.pop()