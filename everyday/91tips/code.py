# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


filepath = "/Users/zhangjiawei/Documents/myshare/wrap/OSZICAR"

f = open(filepath)

contents = f.readlines()
energy = float(contents[-1].strip().split(" ")[4])
print energy
data = []
for i in contents[1:-1]:
    tdata = [t for t in i.strip().split(" ") if t][2:4]
    data.append(tdata)


data = np.array(data, dtype=np.float)
# print data
new_data = data[np.abs(data[:, 1]) <=0.2]
print new_data

plt.hist(new_data[:,0], 200,normed=True)
plt.show()
