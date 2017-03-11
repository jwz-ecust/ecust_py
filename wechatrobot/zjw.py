import matplotlib.pyplot as plt
import numpy as np
# fig = plt.figure()
# ax = fig.add_subplot(111)

x, y = np.random.rand(2, 100)
# print(x, y)

# line = ax.plot(x, y)
# zjw = ax.plot(x **2, y**3)
#
# plt.show()

fig, ax = plt.subplots()
rect1 = plt.Rectangle((0,0), width=1, height=1)
rect2 = plt.Rectangle((1,1), width=1, height=1)
rect3 = plt.Rectangle((2,2), width=1, height=1)
rect4 = plt.Rectangle((3,3), width=1, height=1)
rect4 = plt.Rectangle((0,3), width=1, height=1)

ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)

ax.autoscale_view()

plt.show()
