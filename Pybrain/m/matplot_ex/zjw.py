#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/26
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pylab as plt


mu = 111
sigma = 15
x = mu + sigma*np.random.randn(1000)

num_bins = 50

n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)

y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel("Probability")
plt.title(r"Histogram of IQ: $mu=100$, $\sigma=15$")

plt.subplots_adjust(left=0.15)
plt.savefig('zjw.jpg', bbox_inches='tight', dpi=800)
plt.show()
