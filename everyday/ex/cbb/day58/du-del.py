#!/usr/bin/python
import os
with open('du-files','r') as f:
    for item in iter(f):
        zjw = item.split('\t')
        if 'G' in zjw[0]:
            dd = zjw[1].strip('\n')
            print 'starting deling'+ dd
            os.remove(dd)
    print 'Deleting Done'