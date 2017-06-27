import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
n = 10
a = np.random.random((n, n))
pearsons = a*a.T*10
features = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
coordinate = np.random.random((n, 2))
fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(coordinate[:, 0], coordinate[:, 1])
bbox_props = dict(boxstyle="circle,pad=0.3", fc="cyan", ec="b", lw=2)

for i in range(n):
    t = ax.text(coordinate[i][0], coordinate[i][1], features[i], ha="center", va="center", rotation=45, size=15, bbox=bbox_props)
    # ax.annotate(features[i], xy=coordinate[i], textcoords='data')
for i in range(n):
    for j in range(i, n):
        plt.plot((coordinate[i][0],coordinate[j][0]),(coordinate[i][1],coordinate[j][1]), linewidth=abs(pearsons[i][j]))
        # ax.annotate("", xy=(coordinate[i]), xytext=(coordinate[j]), textcoords='data', arrowprops=dict(arrowstyle="-", width=1.0, connectionstyle="angle3"))

plt.show()