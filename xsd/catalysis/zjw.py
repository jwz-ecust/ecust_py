import shutil
import os


def cpfile(sourcedir, tardir):
    for file in os.listdir(sourcedir):
        file_path = os.join(sourcedir, file)
        shutil.copy(file_path, tardir)


#  复制某个目录下所有文件到目标目录  (可以复制到多个目录)
