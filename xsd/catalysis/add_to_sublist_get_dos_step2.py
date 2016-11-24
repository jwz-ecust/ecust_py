# -*- coding: utf-8 -*-
import os
import shutil
import subprocess


def get_running_dirs():
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

    return runlist


# 获取所有当前作业运行的目录, 返回列表
runlist = get_running_dirs()
work_dir = '/home/users/jwzhang/machine-learning-data/NiP-ads/work'
save_file = '/home/users/jwzhang/sublist'

dirs = os.listdir(work_dir)
with open(save_file, 'wa') as fuck:
    for i in dirs:
        if i.startswith('USPEX'):      # 排除108, 还没跑
            slab_path = work_dir + '/' + i
            dos_path_1 = work_dir + '/' + i + '/dos_cal/step1'
            dos_path_2 = work_dir + '/' + i + '/dos_cal/step2'
            # 判断dos_step_1是否在队列中, 是否投掉作业
            if dos_path_1 not in runlist and os.path.exists(os.path.join(dos_path_1, 'CHGCAR')):
                fuck.write(dos_path_2 + '\n')
                shutil.copy(os.path.join(dos_path_1, 'CHGCAR'), dos_path_2)
                shutil.copy(os.path.join(dos_path_1, 'CONTCAR'), dos_path_2)
                print dos_path_2
