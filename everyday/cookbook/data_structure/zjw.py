def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {"x": 1, 'y':2}, {'x':2, 'y':4}]
zjw = list(dedupe(a, key=lambda d: d['x']))
print(zjw)

a = [11,22,33,33,5,2,1,9,1,5,10]
print(list(dedupe(a)))

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {"x": 1, 'y':2}, {'x':2, 'y':4}]
f = lambda d: d['x']
for i in a:
    print(f(i))


words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look',
'into', 'my', 'eyes', "you're", 'under'
]
words2 = [
'look', "zjw", 'my', 'eyes', "you're", 'under'
]
from collections import Counter
cc = Counter(words)
cc2 = Counter(words2)

print(cc)
print(cc.most_common(3))


C = cc + cc2
print(dir(C))
print(C.keys())
