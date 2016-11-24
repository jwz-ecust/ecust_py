# -*- coding: utf-8 -*-
import os
import subprocess

'''
遍历目录的所有job目录
1. 判断是否运行,
2. 是否满足投作业要求,
3. 是否已经在sublist里面
==> 匹配就讲目录写入sublist

'''

sublist_path = '/home/users/jwzhang/sublist'
path = '/home/users/jwzhang/machine-learning-data/NiP-ads/work'

# 读取 sublist
file = open(sublist_path, 'r')
sublist = [_.strip() for _ in file.readlines() if _]
file.close()

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

print runlist

path_list = []
requirement = ['INCAR', 'KPOINTS', 'POTCAR', 'POSCAR', 'vasp.script']
for i in os.walk(path):
    flag = True
    for _ in requirement:
        temp_path = os.path.join(i[0], _)
        if not os.path.exists(temp_path):
            flag = False
            break
    if flag:
        out_path = os.path.join(i[0], 'OUTCAR')
        # os.path.exists(out_path) 判断是否已经在跑或者跑完
        """需要判断 当前路径是否在 sublist 或者 runlist???"""
        if not any([os.path.exists(out_path), i[0] in runlist, i[0] in sublist]):
            print i
            path_list.append(i[0])

with open(sublist_path, 'wa') as fck:
    for i in path_list:
        fck.write(i + '\n')
