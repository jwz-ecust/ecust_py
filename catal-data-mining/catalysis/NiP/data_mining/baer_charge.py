import os
import subprocess


path = "/home/users/jwzhang/machine-learning-data/NiP-ads/work"

for i in range(1, 111):
    chgcar = path + '/USPEX_generation_{}/dos_cal/step1/CHGCAR'.format(i)
    dos = path + "/USPEX_generation_{}/dos_cal/step1".format(i)
    os.chdir(dos)
    subprocess.check_output(['/home/apps/vasp/bader', chgcar])
    print "finish bader:" + chgcar
