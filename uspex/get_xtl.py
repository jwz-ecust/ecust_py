# -*- coding:utf-8 -*-
import numpy as np


def get_xtl(gatheredposcars_path, template_path='/Users/zhangjiawei/Code/zjw/uspex/template.xtl'):
    # 将poscars的信息一次读取, 一步一步处理
    # 读取模板, 并将信息写入并存储
    with open(gatheredposcars_path) as gp:
        content = gp.readlines()
        num_of_pos = content.count('1.0000\n')
        num_of_each = len(content) / num_of_pos
        for i in range(num_of_pos):
            new_content = []
            file_name = 'USPEX_generation_{}'.format(i)
            title_line = 'TITLE   EA1 _generation_{}.xtl\n'.format(i)
            new_content.append(title_line)
            new_content.append('CELL\n')
            lattice_info = content[i * num_of_each + 2:i * num_of_each + 5]
            lattice = latConverter(lattice_info)
            atom_type = ['Ni', 'P']
            atom_number = content[i * num_of_each + 5].strip().split('   ')
            # generate atom dictionary
            atom = dict(zip(atom_type, atom_number))
            atom_coordinates = content[
                i * num_of_each + 7: (i + 1) * num_of_each - 1]
            lattice_line = '     '.join(
                ['{0:6f}'.format(i) for i in lattice]) + '\n'
            new_content.append(lattice_line)
            new_content.append('SYMMERY  NUMBER  1\n')
            new_content.append('SYMMETRY  LABEL  P1\n')
            new_content.append('ATOMS\n')
            new_content.append('NAME        	X           	Y           	Z\n')
            coordinate_lines = coordinateConverter(atom_coordinates, atom)
            new_content.extend(coordinate_lines)
            new_content.append('EOF\n')
            with open(file_name, 'w') as fuck:
                fuck.writelines(new_content)


def filter_blank(line):
    '''
    filter blank in  a given list
    '''
    return [_ for _ in line if _]


def latConverter(input):
    # 将矩阵转换成晶胞参数 并返回
    output = np.zeros(6)
    x = np.array(filter_blank(input[0].strip().split(' ')), dtype=np.float)
    y = np.array(filter_blank(input[1].strip().split(' ')), dtype=np.float)
    z = np.array(filter_blank(input[2].strip().split(' ')), dtype=np.float)
    output[0] = np.sqrt(sum(np.square(x)))
    output[1] = np.sqrt(sum(np.square(y)))
    output[2] = np.sqrt(sum(np.square(z)))
    output[3] = np.arccos(x.dot(y) / (output[0] * output[1])) * 180.0 / np.pi
    output[4] = np.arccos(x.dot(z) / (output[0] * output[2])) * 180.0 / np.pi
    output[5] = np.arccos(y.dot(z) / (output[1] * output[2])) * 180.0 / np.pi
    return output


def coordinateConverter(input, atom):
    # give input coordinate and atom dictionary
    # 读取坐标, 返回一个元素和坐标的信息
    lines = []
    for atom_type in atom.keys():
        for i in range(int(atom[atom_type])):
            tt = filter_blank(input[i].strip().split())
            t = atom_type.rjust(2) + ' ' * 11 + '     '.join(tt) + '\n'
            lines.append(t)
    return lines


path = '/Users/zhangjiawei/Code/zjw/uspex/gatheredPOSCARS'
get_xtl(path)
