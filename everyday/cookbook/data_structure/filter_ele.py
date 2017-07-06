addresses = [ '5412 N CLARK',
              '5148 N CLARK',
              '5800 E 58TH',
              '2122 N CLARK'
              '5645 N RAVENSWOOD',
              '1060 W ADDISON',
              '4801 N BROADWAY',
              '1039 W GRANVILLE']

counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [i > 5 for i in counts]  # 创建一个布尔序列
from itertools import compress

# for j in compress(addresses, more5):
#     print(j)



prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    }


pp = {key: value for key, value in prices.items() if value > 200}
print(pp)


from collections import namedtuple

zjw = namedtuple("zhangjiawei", ['height', 'weight'])
zz = zjw(180, 180)
print(zz.height)

print(zz)
