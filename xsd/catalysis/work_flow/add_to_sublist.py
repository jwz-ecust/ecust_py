# -*- coding: utf-8 -*-
import os

'''
遍历目录的所有job目录
判断是否运行, 是否满足投作业要求
匹配就讲目录写入sublist

'''


sublist_path = '/home/users/jwzhang/sublist'
path = '/home/users/jwzhang/machine-learning-data/NiP-ads/work'
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
        if not os.path.exists(os.path.join(i[0], 'OUTCAR')):
            path_list.append(i[0])

with open(sublist_path, 'w') as fck:
    for i in path_list:
        fck.write(i + '\n')
