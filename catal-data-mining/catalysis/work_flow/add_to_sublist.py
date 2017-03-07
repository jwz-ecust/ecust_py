# -*- coding: utf-8 -*-
import os
import re
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


class add_to_sublist(object):

    def __init__(self, top_path, sub_dir="/home/users/jwzhang/sublist"):
        self.top_path = top_path
        self.sub_dir = sub_dir
        self.sublist = []
        self.runlist = []
        self.iterlist = []
        self._get_runlist()
        self._get_sublist()
        self._iteration()

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

    def _iteration(self):
        for sub in os.walk(self.top_path):
            self.iterlist.append(sub[0])

    def _check(self, path):
        outcar = os.path.join(path, 'OUTCAR')
        if os.path.exists(outcar):
            if path in self.runlist:
                print "the job in {} is stilling runing".format(path)
            else:
                final_force = self._get_force(outcar)
                if final_force <= 0.05:
                    print "this job in {} has been finished".format(path)
                else:
                    if 'dos' not in path:
                        print "the force in {} is not converge".format(path)
                        origin_file_list = [
                            'INCAR', 'KPOINTS',
                            'POTCAR', 'POSCAR',
                            'vasp.script', 'CONTCAR']
                        for temp in os.listdir(path):
                            ttt = os.path.join(path, temp)
                            cont = os.path.join(path, 'CONTCAR')
                            pos = os.path.join(path, 'POSCAR')
                            if os.path.isfile(ttt) and temp not in origin_file_list:
                                os.remove(ttt)
                        os.rename(cont, pos)
                        sublist.append(path)
        else:
            if path in self.sublist or path in self.runlist:
                print "This job in {} is in Queue! Just waiting!".format(path)
            else:
                if self._check_requirement(path):
                    print "This job in {} would be added to sublist!".format(path)
                    self.sublist.append(path)
                else:
                    if "step2" in path:
                        step1 = path[:-1] + '1'
                        _chgcar = os.path.join(step1, 'CHGAR')
                        _poscar = os.path.join(step1, 'CONTCAR')
                        if os.path.exists(_chgcar) and os.path.exists(_poscar):
                            shutil.copy(_chgcar, path)
                            shutil.copy(_poscar, path)
                            self.sublist.append(path)
                    else:
                        print "This job in {} is not complete".format(path)

    def _get_force(self, outcar):
        output = subprocess.check_output(['grep', 'FORCES:', outcar])
        return float(output.strip().split('\n')[-1].split(" " * 4)[1])

    def all_walk(self):
        for sub in self.iterlist:
            self._check(sub)
        self.tosubfile()


top_path = '/home/users/jwzhang/machine-learning-data/NiP-ads/work'
zjw = add_to_sublist(top_path)

zjw.all_walk()
