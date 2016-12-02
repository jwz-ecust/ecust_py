# -*- coding:utf-8 -*-
# author: zjw@ecust
# gayhub  https://github.com/jwz-ecust

import numpy as np
import sys
import os


def get_xtl(gather_pos_path):
    with open(gather_pos_path) as gp:
        content = gp.readlines()
        num_of_pos = content.count('Direct\n')
        num_of_each = len(content) / num_of_pos
        for i in range(num_of_pos):
            new_content = []
            # 生成文件名
            file_name = '{}_POSCAR'.format(i + 1)
            c = [_ for _ in content[i * num_of_each].split(' ') if _][1:4][-1]
            # 文件第一行
            title_line = '{} generated POSCAR by zjw\n'.format(i + 1)
            latt = content[i * num_of_each + 2:i * num_of_each + 5]
            new_latt = get_lattice(latt)
            new_content.append(title_line)
            new_content.append('1.0000\n')
            new_content.extend(new_latt)
            new_content.extend(
                content[i * num_of_each + 5: i * num_of_each + 7])
            new_content.append('Selective dynamics\n')
            new_content.append('Direct\n')
            coordinates = content[i * num_of_each + 8: (i + 1) * num_of_each]
            new_coordinates = coordinate_z_half(coordinates)
            new_content.extend(new_coordinates)
            with open(file_name, 'w') as fuck:
                fuck.writelines(new_content)


def get_lattice(latt):
    abc = np.zeros((3, 3), dtype=np.float)
    for i in range(3):
        a = [float(_) for _ in latt[i].strip().split(" ") if _]
        abc[i] = a
    abc[2, 2] = abc[2, 2] + 10
    _latt = []
    for i in abc:
        _latt.append('  ' + '    '.join([str(_).rjust(9) for _ in i]) + '\n')
    return _latt


def coordinate_z_half(coordinates):
    _coordinates = []
    length = len(coordinates)
    xyz = np.zeros((length, 3), dtype=np.float)
    for i in range(length):
        xyz[i] = [float(_) for _ in coordinates[i].strip().split(' ') if _]
    for i in xyz:
        i[2] = i[2] / 2
        _coordinates.append(
            "  " + '     '.join([str(_t).ljust(8) for _t in i]) + '\n')
    return _coordinates


gather_pos_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/Ni2P/Ni2P_gatheredPOSCARS"
get_xtl(gather_pos_path)
