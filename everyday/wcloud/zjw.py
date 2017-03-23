import os
import shutil
import subprocess

work = "/home/riic/gdata/home/zjw/mldata/relax"
files = os.listdir(work)

source = "/home/riic/gdata/home/zjw/mldata/vasp.script"

for i in files:
    to = work + "/" + i + "/vasp.script"
    os.chdir(work + "/" + i)
    subprocess.call(['qsub', 'vasp.script'])
