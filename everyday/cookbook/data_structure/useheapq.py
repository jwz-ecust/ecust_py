import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        print(item)
        print(priority)
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)



q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('zjw'), 2)
q.push(Item("cbb"), 1)


print(q.pop())
