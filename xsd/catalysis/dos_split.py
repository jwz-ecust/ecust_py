# -*- coding: utf-8 -*-
import re
import os
import numpy as np

cwd = os.getcwd()
dos_path = os.path.join(cwd, 'DOSCAR')
# incar_path = os.path.join(cwd, 'INCAR')
outcar_path = os.path.join(cwd, 'OUTCAR')


def clean_null(l):
    return [_ for _ in l if _]


def _get_feimi(path):
    with open(outcar_path, 'r') as f1:
        a = f1.readlines()
        for item in a:
            if 'E-fermi' in item:
                fermi = item.split(':')[1].strip().split(' ')[0]
    return fermi


def _split(dos_path, n_site=None):
    '''
    分割 投影在原子上的DOS
    如果没有指定哪个site序号,就输出所有的分DOS
    如果指定了具体的Site序号, 则输出这个原子的分DOS
    横坐标没有减去 费米能级
    在 get-d-band-center 中处理
    n_site 就是 实际对应的原子序号(从1 开始)
    生成DOS0 是总的DOS
    '''
    g_dos_path = os.path.dirname(dos_path)
    with open(dos_path, 'r') as fuck:
        number = int(fuck.readline().strip().split(' ')[0])
        for i in range(4):
            fuck.readline()
        content = fuck.readlines()
        sub_n = int(clean_null(content[0].strip().split('  '))[2])
        sub_n = sub_n + 1
        if n_site == None:
            for i in range(number + 1):
                dos_name = os.path.join(g_dos_path, 'DOS{}'.format(str(i)))
                with open(dos_name, 'w') as fyou:
                    fyou.writelines(
                        content[i * sub_n + 1: (i + 1) * sub_n])
        else:
            dos_name = os.path.join(g_dos_path, 'DOS{}'.format(str(n_site)))
            with open(dos_name, 'w') as fher:
                fher.writelines(
                    content[n_site * sub_n + 1:(n_site + 1) * sub_n])


def get_d_band_center(path, feimi):
    dos_data = np.loadtxt(path)
    dos_data[:, 0] = dos_data[:, 0] - feimi
    length = dos_data.shape[0]
    sum_multi = 0
    sum = 0
    for i in range(length - 1):
        delta = dos_data[i + 1, 0] - dos_data[i, 0]
        sum_multi = sum_multi + delta * \
            dos_data[i + 1, -1] * dos_data[i + 1, 0]
        sum = sum + delta * dos_data[i + 1, -1]
    return sum_multi / sum


_split(dos_path)
