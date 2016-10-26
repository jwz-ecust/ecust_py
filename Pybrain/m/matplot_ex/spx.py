#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 16/10/26

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import pandas as pd


fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
data = pd.read_csv('./spx.csv', index_col=0, parse_dates=True)
spx = data['SPX']
spx.plot(ax=ax, style='k-')

crisis_data = [
    (datetime(2007, 10, 11), 'Peak of bull market'),
    (datetime(2008, 3 ,12), 'Bear Strearns Fails'),
    (datetime(2008, 9, 15), 'Lehman Bankruptcy')
]


for date, label in crisis_data:
    ax.annotate(label, xy=(date, spx.asof(date)+50),
                xytext=(date, spx.asof(date)+200),
                arrowprops=dict(facecolor='black'),
                horizontalalignment='left',
                verticalalignment='top'
                )

ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])
ax.set_title("Import dates in 2008-2009 financial crisis")

ax1 = fig.add_subplot(2, 2, 4)
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color='k', alpha=0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color='b', alpha=0.4)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]], color='g', alpha=0.5)
ax1.add_patch(rect)
ax1.add_patch(circ)
ax1.add_patch(pgon)

fig.savefig('figpath.jpg', dpi=500, bbox_inches='tight')
plt.show()
