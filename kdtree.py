import numpy as np
from itertools import cycle
import matplotlib.pyplot as plt
import sys


def plotline(c1, c2):
    """
    c1: x 取值范围
    c2: y 取值范围
    """
    if not np.alltrue(c1==c1[0]):
        p = np.polyfit(c1, c2, 1)
        pp = np.poly1d(p)
        xx = np.linspace(c1[0], c1[1], 100)
        plt.plot(xx, pp(xx), linewidth=3)
    else:
        yy = np.linspace(c2[0], c2[1], 50)
        xx = np.zeros(len(yy))
        xx[:] = c1[0]
        plt.plot(xx, yy)


def splitX(X, X_min, Y_min, X_max, Y_max, s=0):
    if len(X) < 2:
        return
    
    if s == 0:
        s = 1
        X_median = np.median(X[:, s])

        # left
        X_left = X[X[:,s] < X_median]
        X_left_min = X_min
        X_left_max = X_median
        Y_left_min = Y_min
        Y_left_max = Y_max

        # right
        X_right = X[X[:,s] >= X_median]
        X_right_min = X_median
        X_right_max = X_max
        Y_right_min = Y_min
        Y_right_max = Y_max

        # plot
        plotline((X_median, X_median), (Y_min, Y_max))

        return splitX(X_left, X_left_min, Y_left_min, X_left_max, Y_left_max, s=s), splitX(X_right, X_right_min, Y_right_min, X_right_max, Y_right_max, s=s)

    if s == 1:
        s = 0
        Y_median = np.median(X[:, s])
        # down
        Y_down = X[X[:, s] < Y_median]

        X_down_max = X_max
        X_down_min = X_min
        Y_down_min = Y_min
        Y_down_max = Y_median

        # top
        Y_top = X[X[:,s] >= Y_median]
        X_top_max = X_max
        X_top_min = X_min
        Y_top_min = Y_median
        Y_top_max = Y_max

        # plot
        plotline((X_min, X_max), (Y_median, Y_median))

        return splitX(Y_down, X_down_min, Y_down_min, X_down_max, Y_down_max, s=s), splitX(Y_top, X_top_min, Y_top_min, X_top_max, Y_top_max, s=s)


sys.setrecursionlimit(20000)
plt.figure()
np.random.seed(1)
X = np.random.randint(0,50, size=(50,2))
plt.scatter(X[:, 0], X[:, 1])
X_min = 0
Y_min = 0
X_max = np.max(X[:, 0])
Y_max = np.max(X[:, 1])
plotline([0, X_max], [Y_max, Y_max])
plotline([X_max, X_max], [0, Y_max])


splitX(X, X_min, Y_min, X_max, Y_max)
plt.show()
