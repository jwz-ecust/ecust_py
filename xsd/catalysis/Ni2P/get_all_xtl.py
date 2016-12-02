# -*- coding:utf-8 -*-
# author: zjw@ecust
# gayhub  https://github.com/jwz-ecust
'''
################################################################################
just need to input the atom type in seque
this script would generate all structure according to gatheredPOSCARS
################################################################################
'''
import numpy as np
import sys
import os


def get_xtl(gather_pos_path):
    with open(gather_pos_path) as gp:
        content = gp.readlines()
        num_of_pos = content.count('1.0000\n')
        num_of_each = len(content) / num_of_pos
        for i in range(num_of_pos):
            new_content = []
            # 生成文件名
            file_name = 'USPEX_generation_{}.xtl'.format(i + 1)
            # 文件第一行
            title_line = 'TITLE   EA1 _generation_{}.xtl\n'.format(i + 1)
            new_content.append(title_line)
            # 第二行 CELL
            new_content.append('CELL\n')
            lattice = content[i * num_of_each + 2:i * num_of_each + 5]
            lattice_info = _latConverter(lattice)

            atom_type = content[i * num_of_each + 5].strip().split('   ')
            atom_number = content[i * num_of_each + 6].strip().split('   ')
            # generate atom list[tuple]
            atom = zip(atom_type, atom_number)

            atom_coordinates = content[
                i * num_of_each + 7: (i + 1) * num_of_each]
            lattice_line = '     '.join(
                ['{0:6f}'.format(i) for i in lattice_info]) + '\n'

            new_content.append(lattice_line)
            new_content.append('SYMMERY  NUMBER  1\n')
            new_content.append('SYMMETRY  LABEL  P1\n')
            new_content.append('ATOMS\n')
            new_content.append('NAME        	X           	Y           	Z\n')
            coordinate_lines = _coordinateConverter(atom_coordinates, atom)
            new_content.extend(coordinate_lines)
            new_content.append('EOF\n')
            with open(file_name, 'w') as fuck:
                fuck.writelines(new_content)


def _filter_blank(line):
    '''
    filter blank in  a given list
    '''
    return [_ for _ in line if _]


def _latConverter(input):
    '''
    give lattice matrix
    return    lattice parameters a,b, c, angle
    '''

    lattice_abc = np.zeros((3, 3))
    for i in range(3):
        lattice_abc[i] = np.array(_filter_blank(
            input[i].strip().split(' ')), dtype=np.float)
    # SVD
    abc = []
    for i in range(3):
        abc.append(np.linalg.norm(lattice_abc[i]))
    # norm
    # _, abc, _ = np.linalg.svd(lattice_abc)
    # lattice_abc = np.diag(abc)
    lattice_angle = []

    for i in range(len(abc)):
        for j in range(i + 1, len(abc)):
            num = lattice_abc[i].dot(lattice_abc[j])
            demon = np.linalg.norm(
                lattice_abc[i]) * np.linalg.norm(lattice_abc[j])
            angle = np.arccos(num / demon) * 180 / np.pi
            lattice_angle.append(angle)

    return list(abc) + lattice_angle


def _coordinateConverter(input, atom):
    # give input coordinate and atom dictionary
    lines = []
    atom_type_number = len(atom)
    cont = 0
    for i in range(atom_type_number):
        each_atom_number = int(atom[i][1])
        for j in range(each_atom_number):
            tt = _filter_blank(input[cont].strip().split())
            t = atom[i][0].ljust(2) + ' ' * 11 + '     '.join(tt) + '\n'
            lines.append(t)
            cont = cont + 1
    return lines


if __name__ == '__main__':
    gather_pos_path = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/Ni2P/Ni2P_gatheredPOSCARS'
    get_xtl(gather_pos_path)
