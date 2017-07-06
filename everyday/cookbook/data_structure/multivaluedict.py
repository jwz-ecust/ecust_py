# multi values dict
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append("zjw")
d['a'].append([1,1,1,0])
# print(d)


p = defaultdict(set)
p['newset'].add(1)
p['newset'].add(115)
p['newset'].add(11235123)
p['newset'].add(13)
p['newset'].add(2)
# print(p)

# ordered dict
from collections import OrderedDict
def ordered_dict():
    d = OrderedDict()
    d['foor'] = 1
    d['abc'] = 2
    d['spam'] = 3
    d['zzz'] = 4
    print(d)

ordered_dict()
