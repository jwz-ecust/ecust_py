import numpy as np
from itertools import cycle
import matplotlib.pyplot as plt


def plotline(c1, c2):
    """
    c1: x 取值范围
    c2: y 取值范围
    """
    p = np.polyfit(c1, c2, 1)
    pp = np.poly1d(p)
    xx = np.linspace(c1[0], c1[1], 100)
    plt.plot(xx, pp(xx), linewidth=3)


a = np.array([0, 100])
b = np.array([0, 100])
plt.figure()
plotline(a, b)
plt.show()