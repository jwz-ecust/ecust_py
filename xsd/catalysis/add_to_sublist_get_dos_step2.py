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

# 获取所待投作业目录, 返回列表
file = open(save_file, 'r')
sublist = [_.strip() for _ in file.readlines() if _]
file.close()


dirs = os.listdir(work_dir)
with open(save_file, 'a') as fuck:
    for i in dirs:
        slab_path = work_dir + '/' + i
        dos_path_1 = work_dir + '/' + i + '/dos_cal/step1'
        dos_path_2 = work_dir + '/' + i + '/dos_cal/step2'
        # 判断dos_step_1是否在队列中, 是否投掉作业
        if dos_path_1 not in runlist and dos_path_2 not in sublist and os.path.exists(os.path.join(dos_path_1, 'CHGCAR')):
            fuck.write(dos_path_2 + '\n')
            # shutil.copy 使用类似与linux中的cp命令
            # 指定待复制的文件和复制到目录的文件(文件名可指定)
            shutil.copy(os.path.join(dos_path_1, 'CHGCAR'), dos_path_2)
            shutil.copy(os.path.join(dos_path_1, 'CONTCAR'),
                        os.path.join(dos_path_2, 'POSCAR'))
            print dos_path_2
