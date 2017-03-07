# -*- coding: utf-8 -*-
import shutil
import os


def cpfile(sourcedir, tardir):
    '''
    复制某个目录下所有文件到目标目录  (可以复制到多个目录)
    '''
    for file in os.listdir(sourcedir):
        file_path = os.path.join(sourcedir, file)
        shutil.copy(file_path, tardir)


sourcedir = '/home/users/jwzhang/machine-learning-data/NiP-ads/model'
basedir = '/home/users/jwzhang/machine-learning-data/NiP-ads/work'

aaa = "USPEX_generation_20"

for i in range(1, 111):
    tardir = basedir + "/USPEX_generation_{}".format(str(i)) + '/dos_cal/step2'
    cpfile(sourcedir, tardir)
