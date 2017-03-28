import shutil
import os
import subprocess

work_path = "/home/riic/gdata/home/zjw/dos"
vaspscript_paht = "/home/riic/gdata/home/zjw/mldata／vasp.script"
subpaths = os.listdir(work_path)

for sub in subpaths:
    os.chdir(work_path + "/" + sub + "/step1")
    shutil.copy(work_path + "/CONTCAR", "./POSCAR")
    shutil.copy(vaspscript_paht, "./vasp.script")
    subprocess.call(["qsub", "vasp.script"])
