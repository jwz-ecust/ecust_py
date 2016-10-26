#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/26

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum(), label='one')
ax.plot(np.random.randn(1000).cumsum(), label='two')
ax.plot(np.random.randn(1000).cumsum(), label='three')
ax.plot(np.random.randn(1000).cumsum(), label='four')
ax.plot(np.random.randn(1000).cumsum(), label='five')
ax.legend(loc='best')

tricks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
                            rotation=30, fontsize='small')
ax.set_title("Random Sum Plot")
ax.set_xlabel('Stages')
fig.savefig('my_first.pdf', bbox_inches='tight', dpi=800)
fig.show()
