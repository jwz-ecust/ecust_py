# -*- coding: utf-8 -*-
import subprocess
import re
import os

runlist = []

# 获取在队列中的job的目录列表
qstat_info = subprocess.check_output("qstat -f", shell=True)
qstat_ = qstat_info.split("Job Id: ")
for item in qstat_:
    item = item.split("    ")
    id = item[0]

    for tag in item:
        if "job_state" in tag:
            status = tag.split('=')[-1].strip()
            if status == 'C':
                break

        if "Output" in tag:
            out = tag.split('=')[-1].strip().split(':')[-1]
            pattern = re.compile(r'\n|\t')
            out = re.sub(pattern, '', out)
            out = os.path.dirname(out)
            runlist.append((id.strip(), out))

for i in runlist:
    print i[0], "    ", i[1]
