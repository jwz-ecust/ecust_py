# -*- coding: utf-8 -*-
import subprocess
import re
import os
import logging
import sys
'''
1. 读取sublist 内作业的目录
2. qstat -f 提取运行下(Q+R)的作业目录
3. 如果sublist的目录 存在qstat -f 中, 则从sublist 中删除
4. 如果sublist的目录不在运行, 则投作业
        -如果投作业成功, 删掉对应目录
        -如果投作业失败, 不删掉

==> 新增: 根据运行作业数量, 计算还可以投多少作业.XXX (容易出错)
====> 一旦qsub 超过限制, 则立马退出程序 (这样可以避免计算作业数量)
'''

# create logger
logger_name = "qsub_job"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)
# create file handler
log_path = '/home/users/jwzhang/qsub_job.log'
fh = logging.FileHandler(log_path)
fh.setLevel(logging.INFO)

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)

sub_dir = '/home/users/jwzhang/sublist'
# 待投作业目录列表
file = open(sub_dir, 'r')
sublist = file.readlines()
file.close()
runlist = []

# 获取在队列中的job的目录列表
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


with open(sub_dir, 'w') as fff:
    # 检查作业是否有这五个文件
    input_files = ['INCAR', 'KPOINTS', 'POSCAR', 'POTCAR', 'vasp.script']
    for sub in sublist:
        i = sub.strip()
        # 检查 INCAR POTCAR KPOINTS vasp.script POSCAR是否齐全
        try:
            os.chdir(i)
        except OSError as e:
            logger.info("directory file not exists")
        else:
            if all([os.path.exists(_) for _ in input_files]):
                if i.strip() not in runlist:
                    vasp_script = os.path.join(i, 'vasp.script')
                    try:
                        subprocess.check_call(['qsub', vasp_script])
                    except:
                        print "保存下哈哈"
                        fff.writelines(sublist)   # 退出前保存下所有路径
                        logger.info("{} up to submit limit!".format(i))
                        sys.exit("jobs has already up to limit, Bye Bye!")
                    else:
                        print "finish qsub job and now remove the job from sublist"
                        sublist.remove(sub)
                else:
                    logger.debug("job in {} has already in queue".format(i))
                    print "the job in {} is been run, deleting it".format(i)
                    sublist.remove(sub)
            else:
                # 文件不全, 无法投作业
                logger.debug(
                    "something wrong in {}, input files are not complete".format(i))
    fff.writelines()   # 如果不出错, 保存下路径
