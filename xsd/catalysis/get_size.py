import os
from os.path import join, getsize


def getdirsize(dir):
    size = 0L
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name))] for name in files)
    return size

dirs = os.listdir('/home/users/jwzhang')
for i in dirs:
    filesize = getdirsize(join('/home/users/jwzhang', i)
    print "{}'s size is {}".format(i, filesize)
