# -*- coding: utf-8 -*-
import os
import subprocess
import shutil

'''
遍历目录的所有job目录 =======> os.walk(dir)
    判断DOSCAR是否存在
        存在(判断是否在Runlist里?)
            是:
                还在running, 不虚
            否(看Forces是否标准):
                是: ==> 很好
                否: ==> 不然就输出路径重新处理
        不存在(是否在Runlist或者Queuelist中):
            是:
                慢慢等呗
            否(检查五个文件全不全):
                全: ==> 加入QueueList
                不全: ==> 等待编写作业
'''

sublist_path = '/home/users/jwzhang/sublist'
top_path = '/home/users/jwzhang/machine-learning-data/NiP-ads/work'

# 读取 sublist
file = open(sublist_path, 'r')
sublist = file.readlines()
file.close()


def get_run_list():
    # 获取在队列中的job的目录列表 ==> 返回runlist

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


def check_5_inputfiles(path):
    '''
    检查是否存在五个输入文件.....未完待续
    返回 True or False
    '''
    requirement = ['INCAR', 'KPOINTS', 'POTCAR', 'POSCAR', 'vasp.script']
    for tt in requirement:
        temp_path = os.path.join(path, tt)
        if not os.path.exists(temp_path):
            return False
            break
    else:
        return True


# 获取runlist==>
runlist = get_run_list()
# 开始遍历, 同时打开文件准备修改
with open(sublist_path, 'a') as fucku:
    for sub in os.walk(top_path):
        sub_dir = sub[0]
        # 判断路径是否存在OUTCAR
        outcar = os.path.join(sub_dir, 'OUTCAR')
        if os.path.exists(outcar):
            # 判断是否在runlist里面
            if sub_dir in runlist:
                print "This job in {} is still running!".format(sub_dir)
                # 不在runlist里面的话判断是否收敛
            else:
                # 判断是否收敛
                output = subprocess.check_output(['grep', 'FORCES:', outcar])
                final_force = output.strip().split('\n')[-1].split(' ' * 4)[1]
                if float(final_force) <= 0.05:
                    print "This job in {} has been finished!".format(sub_dir)
                else:
                    # 可以复制CONTACAR, 删掉 重投-----to-be-updated
                    # 并且不是DOS路径
                    if 'dos' not in sub_dir:
                        print "the force in {} is not convergence, resubing".format(sub_dir)
                        origin_file_list = [
                            'INCAR', 'KPOINTS',
                            'POTCAR', 'POSCAR',
                            'vasp.script', 'CONTCAR']
                        for _ in os.listdir(sub_dir):
                            if os.path.isfile(os.path.join(sub_dir, _)) and _ not in origin_file_list:
                                os.remove(os.path.join(sub_dir, _))
                        os.rename(os.path.join(sub_dir, 'CONTCAR'),
                                  os.path.join(sub_dir, 'POSCAR'))
                        fucku.write(sub_dir + '\n')

        else:
            _sub_dir = sub_dir + "\n"
            # 检查当前路径是否在runlist 或者 sublist中
            if sub_dir in runlist or _sub_dir in sublist:
                print "This job in {} is Queue! Just waiting!".format(sub_dir)
            else:
                if len(sub[-1]) >= 4:
                    # 检查5个输入文件
                    if check_5_inputfiles(sub_dir):
                        # 满足条件, 并写入sublist
                        print "This job in {} needs to be subed!".format(sub_dir)
                        fucku.write(_sub_dir)
                    else:
                        if 'step2' in sub_dir:
                            step1 = sub_dir[:-1] + '1'
                            try:
                                chgcar = os.path.join(step1, "CHGCAR")
                                _poscar = os.path.join(step1, "POSCAR")
                                shutil.copy(chgcar, sub_dir)
                                shutil.copy(_poscar, sub_dir)
                                fucku.write(_sub_dir)
                            except:
                                pass
                                # 输入文件不全, 待我编写作业
                        else:
                            print "This job in {} need to be written!".format(sub_dir)
