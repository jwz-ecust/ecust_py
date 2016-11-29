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
++++++++ 如果sublist里面空的处理 ==> 直接判断sublist 是否 为空的列表

'''


class batch_qsub(object):

    def __init__(self, sub_dir='/home/users/jwzhang/sublist'):
        self.sub_dir = sub_dir
        self.runlist = []
        self.sublist = []
        self._get_runlist()
        self._get_sublist()

    def _get_runlist(self):
        qstat_info = subprocess.check_output("qstat -f", shell=True)
        qstat_ = qstat_info.split("Job Id: ")
        for item in qstat_:
            item = item.split("    ")
            for tag in item:
                if "job_state" in tag:
                    status = tag.split("=")[-1].strip()
                    if status == "C":
                        break
                if "Output" in tag:
                    out = tag.split('=')[-1].strip().split(":")[-1]
                    pattern = re.compile(r'\n|\t')
                    out = re.sub(pattern, '', out)
                    out = os.path.dirname(out)
                    self.runlist.append(out)

    def _get_sublist(self):
        with open(self.sub_dir, 'r') as fuck:
            for _ in fuck.readlines():
                self.sublist.append(_.strip())

    def _check_requirement(self, path):
        req = ['INCAR', 'KPOINTS', 'POSCAR', 'POTCAR', 'vasp.script']
        if all([os.path.exists(os.path.join(path, _)) for _ in req]):
            return True
        return False

    def remove_path(self, path):
        self.sublist.remove(path)

    def tosubfile(self):
        with open(self.sub_dir, 'w') as f:
            for _ in self.sublist:
                f.write(_ + '\n')

    def qsub(self, path):
        if self._check_requirement(path):
            if path not in self.runlist:
                vasp_script = os.path.join(path, 'vasp.script')
                try:
                    subprocess.check_call(['qsub', vasp_script])
                except Exception as e:
                    self.tosubfile()
                    sys.exit(
                        "Fuck! Job have up to limit! Bye Bye! Error: {}".format(e))
                else:
                    self.remove_path(path)
            else:
                self.remove_path(path)
        else:
            print "The job dir: {} is not satistified!".format(path)
            self.remove_path(path)

    def batch(self):
        if self.sublist != []:
            for path in self.sublist:
                self.qsub(path)
            else:
                self.tosubfile()
        else:
            sys.exit("Sorry, sublist is null, waiting for new jobs!")

if __name__ == "__main__":
    jobs = batch_qsub()
    jobs.batch()
