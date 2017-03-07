# -*- coding: utf-8 -*-
import os
import os.path as op
import subprocess


# 获取在队列中的job的目录列表
runlist = []
qstat_info = subprocess.check_output("qstat -f", shell=True)
qstat_ = qstat_info.split("Job Id: ")
for item in qstat_:
    item = item.split("    ")

    for tag in item:
        if "job_state" in tag:
            status = tag.split('=')[-1].strip()
            if status == 'C':
                break

        if "Output" in tag:
            out = tag.split('=')[-1].strip().split(':')[-1]
            out = ''.join(out.split('\t'))
            out = ''.join(out.split('\n'))
            out = '/'.join(out.split('/')[:-1])
            runlist.append(out)


work_dir = '/home/users/jwzhang/machine-learning-data/Ni2P/work'

lists = os.walk(work_dir)   # return a generator

save_path_text = '/home/users/jwzhang/sublist'
fuck = open(save_path_text, 'a')
force_big_list = []

for sublist in lists:
    outcar = op.join(sublist[0], 'OUTCAR')
    try:
        if sublist[0] not in runlist:
            output = subprocess.check_output(['grep', 'FORCES:', outcar])
            final_force = output.strip().split('\n')[-1].split(' ' * 4)[1]
            if float(final_force) > 0.05:
                fuck.write(sublist[0] + '\n')
                force_big_list.append(sublist[0])
    except:
        # 如果不存在OUTCAR, 说明不是一个作业目录, 或者作业还没有运行
        print "maybe it is not a job dir or be not runned"


for son in force_big_list:
    os.chdir(son)
    os.rename(os.path.join(son, "CONTCAR"), os.path.join(son, "POSCAR"))
    requirement = ["INCAR", "KPOINTS", "vasp.script", "POSCAR", "POTCAR"]
    for i in os.listdir(son):
        _path = os.path.join(son, i)
        if i not in requirement and os.path.isfile(_path):
            os.remove(_path)
