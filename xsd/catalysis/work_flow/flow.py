# -*- coding: utf-8 -*-
import subprocess
import re
import os

sub_dir = '/home/users/jwzhang/sublist'
# 待投作业目录列表
sublist = open(sub_dir, 'r').readlines()
runlist = []

qstat_info = subprocess.check_output("qstat -f", shell=True)
qstat_ = qstat_info.split("Job Id: ")
for item in qstat_:
    item = item.split("    ")

    for tag in item:
        if "job_state" in tag:
            status = tag.split('=')[-1].strip()
            if status == 'C':
                continue

        if "Output" in tag:
            out = tag.split('=')[-1].strip().split(':')[-1]
            out = ''.join(out.split('\t'))
            out = ''.join(out.split('\n'))
            out = '/'.join(out.split('/')[:-1])
            runlist.append(out)

for i in sublist:
    i = i.strip()
    if i not in runlist:
        vasp_script = os.path.join(i, 'vasp.script')
