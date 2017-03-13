import bisect
import random

random.seed(1)
print "New Pos Content"
print "--- --- ----------------------------------------------------------------"
l = []
for i in range(15):
    r = random.randint(1, 100)
    position = bisect.bisect(l, r)
    bisect.insort(l, r)
    print "%3d %3d" % (r, position), l


def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect(breakpoints, score)
    return grades[i]
    '''
    bisect.bisect ===> return the index
    bisect.insert ===> return None, but arrange the element to the list
    '''


print [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
