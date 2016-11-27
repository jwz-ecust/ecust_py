# -*- coding: utf-8 -*-
import os
import os.path as op
import subprocess


# 获取在队列中的job的目录列表
Qlist = []
idlist = []
qstat_info = subprocess.check_output("qstat -f", shell=True)
qstat_ = qstat_info.split("Job Id: ")
for item in qstat_:
    item = item.split("    ")
    id = item[0]

    for tag in item:
        if "job_state" in tag:
            status = tag.split('=')[-1].strip()
            if status == 'C' or status == 'R':
                break

        if "Output" in tag:
            out = tag.split('=')[-1].strip().split(':')[-1]
            out = ''.join(out.split('\t'))
            out = ''.join(out.split('\n'))
            out = '/'.join(out.split('/')[:-1])
            Qlist.append(out)
            idlist.append(id.strip())


print len(Qlist) == len(list(set(Qlist))
