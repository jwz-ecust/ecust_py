#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 12/28/16
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt


markers = ('s', 'x', 'o', '^', 'v')
colors = ('red', 'blue', 'gray', 'cyan')
cmap = ListedColormap(colors[:len(np.unique(y))])


x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
xxx = np.array([xx1.ravel(), xx2.ravel()]).T

Z = Z.reshape(xx1.shape)
plt.contourf(xx1, xx2, Z, slpha=0.4, cmap=cmap)
plt.xlim(xx1.min(), xx1.max())
plt.ylim(xx2.min(), xx2.max())
