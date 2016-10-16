# -*- coding: utf-8 -*-
a = raw_input("请输入数字>>>")
count = int(input("请输入几个数字相加>>>"))
res = []
for i in range(1,count+1):
    res.append(int(a*i))
    print res[i-1]
print sum(res)
