#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/26
import matplotlib.pyplot as plt
import numpy as np


figure = plt.figure()
ax1 = figure.add_subplot(2, 2, 1)
ax2 = figure.add_subplot(2, 2, 2)
ax3 = figure.add_subplot(2, 2, 3)
ax4 = figure.add_subplot(2, 2, 4)
ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30)+10*np.random.randn(30))
ax3.plot(np.random.randn(50), 'k--')
ax4.hist(np.random.randn(100), bins=50, color='k', alpha=0.3)
figure.show()
