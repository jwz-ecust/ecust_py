# -*- coding: utf-8 -*-
# author: jwz-ecust
# mail: jwz_ecust@mail.ecust.edu.cn

import xml.etree.cElementTree as ET
import os
import numpy as np


def read_xsd(file_path):
    '''
    read data from xsd file
    return coordiante_array and atom_list
    Target: 需要读取 原子种类, 原子坐标, 晶胞参数
    '''
    root = ET.ElementTree(file=file_path)
    # get the spacegroup infor
    direction = ['A', 'B', 'C']
    # Xpath 寻找任意属性 .//attribute_name
    spacegroup = root.find(".//SpaceGroup")
    lattice_info = np.zeros((3, 3))
    for i in range(3):
        key_name = '{}Vector'.format(direction[i])
        lattice_info[i] = np.array(spacegroup.get(
            key_name).split(','), dtype=np.float)

    atom_list = []
    coordiante_list = []

    for element in root.iter():

        if 'XYZ' in element.keys() and 'Components' in element.keys():
            atom_name = element.get('Components')
            coordiante = element.get('XYZ').split(',')
            atom_list.append(atom_name)
            coordiante_list.append(coordiante)

    # transform raw XYZ into numpy array
    atom_array = np.array(coordiante_list, dtype=np.float)
    return atom_array, atom_list, lattice_info


def read_contcar(contcar_path):
    '''
    read data from xsd file
    return coordiante_array and atom_list
    Target: 需要读取 原子种类, 原子坐标, 晶胞参数
    return:
            lattice: 3x3 numpy array
            atom: 字典  {'P':14, 'Ni':14}
            atom_array: ['P', 'P', ...., 'Ni',...,'Ni']
            coordinates: 28x3 numpy array
    '''
    with open(contcar_path, 'r') as f:
        info = f.readlines()
        # 获取晶胞参数信息
        _lattice = info[2:5]
        lattice = np.zeros((3, 3), dtype=np.float)
        for i in range(3):
            lattice[i] = [float(_)
                          for _ in _lattice[i].strip().split(' ') if _]

        # 获取元素种类, 数目信息
        atom_type = info[5].strip().split("    ")
        atom_number = [int(_) for _ in info[6].strip().split("    ")]
        total_number = sum(atom_number)
        atom = dict(zip(atom_type, atom_number))
        atom_array = [atom_type[0]] * atom[atom_type[0]] + \
            [atom_type[1]] * atom[atom_type[1]]

        # 获取坐标信息
        coordinate = np.zeros((total_number, 3))

        _coordinates = info[9: 9 + total_number]
        for i in range(total_number):
            temp = [_ for _ in _coordinates[i].strip().split(' ') if _][0:3]
            coordinate[i] = [float(_) for _ in temp]

    return coordinate, atom_array, lattice


# zjw = "/Volumes/WD/data/NiP_data/surface/contcar/CONTCAR_slab_100"
# read_contcar(zjw)


def dis_calculate(i, j, atom_array, lattice_info):
    '''
    this is used to calculate the distence between two atoms
    相对坐标需要转化为绝对坐标
    '''
    abc = lattice_info.diagonal()
    i_ads_coor = atom_array[i] * abc
    j_ads_coor = atom_array[j] * abc
    return np.linalg.norm(i_ads_coor - j_ads_coor)


def coulomb_matrix_calculate(i, j, atom_list, atom_array, lattice_info):
    '''
    this is used to coulomb matrix element
    '''
    charge_info = {'C': 4.0, 'O': 6.0, 'P': 5.0, 'Ni': 10.0}

    if i == j:
        matrix_element = 0.5 * charge_info[atom_list[i]]**2.4
    else:
        matrix_element = charge_info[atom_list[
            i]] * charge_info[atom_list[j]] / dis_calculate(i, j, atom_array, lattice_info)
    return matrix_element


def _get_coulomb_matrix(atom_list, atom_array, lattice_info):
    '''H
    给定坐标, 原子种类, 和晶胞参数信息
    计算库伦矩阵
    '''
    length = atom_array.shape[0]
    cou_matrix = np.zero((length, length))
    for i in range(length):
        for j in range(length):
            cou_matrix[i][j] = coulomb_matrix_calculate(
                i, j, atom_list, atom_array, lattice_info)
    return cou_matrix


def extract_local_structure(atom_array, atom_list, site_ID, lattice_info, n=10):
    '''
    需要输入 坐标数据, 元素种类 以及吸附site的序号(site_ID),  以及局部结构的原子总数(n)
    返回 (元素种类, 序号, 距离, 元素坐标)
    '''
    locals = []
    ads_site = atom_array[site_ID]
    for i in range(len(atom_list)):
        if i == site_ID:
            locals.append([atom_list[i], i, 0.0, atom_array[i][
                          0], atom_array[i][1], atom_array[i][2]])
        else:
            distence = dis_calculate(i, site_ID, atom_array, lattice_info)
            locals.append([atom_list[i], i, distence, atom_array[i][
                          0], atom_array[i][1], atom_array[i][2]])
    return sorted(locals, key=lambda x: x[2])[1:n + 1]


def find_the_max_site(atom_array, atom_list):
    length = len(atom_list)
    Ni_list = []
    for i in range(length):
        if atom_list[i] == 'Ni':
            Ni_list.append(i)
    Ni_array = np.zeros(len(Ni_list), dtype=np.float)
    for i in range(len(Ni_list)):
        temp = atom_array[Ni_list[i]][2]
        Ni_array[i] = temp
    return Ni_list[Ni_array.argmax()]


def bond_angle_cal(i_array, j_array):
    # 角度计算, 余弦,  反三角函数
    dot_product = i_array.dot(j_array)
    i = np.linalg.norm(i_array)
    j = np.linalg.norm(j_array)
    return np.arccos(dot_product / (i * j)) * 180 / np.pi


def local_structure_cal(locals, site_ID, atom_array, lattice_info):
    '''
    计算局部结构的信息
    返回 键长, 键角
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    考虑与吸附 Site(Ni) 最近的10个原子 (这里先考虑10个原子)
        1. distance  finished
        2. 夹角 (考虑 Ni-C 键反向与X, Z轴方向的夹角)  C: Coordinate
        3. 原子的电负性 (考虑中) ===> 包含在 库伦矩阵中???
        4. d-band center (未考虑)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    '''
    X_axis = np.array([1.0, 0.0, 0.0])
    Z_axis = np.array([0.0, 0.0, 1.0])

    fix_vector = Z_axis
    # fix_vector is along the Z axis  [0., 0., 0.49001]
    info_local_structure = []
    for i in locals:
        sub_bond_vec = i[-1] - atom_array[site_ID]
        angle_Y = bond_angle_cal(Z_axis, sub_bond_vec)
        angle_X = bond_angle_cal(X_axis, sub_bond_vec)
        info_list = [str(m) for m in i]
        info_list.extend([str(angle_X), str(angle_Y)])
        info_local_structure.append(info_list)
    return info_local_structure


'''
================================================================================
starting mining
================================================================================
'''

# giving the contcar file
# zjw = "/Volumes/WD/data/NiP_data/surface/contcar/CONTCAR_slab_100"

zjw = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP/data_mining/CONTCAR"

# path = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP_001-u.xsd'

atom_array, atom_list, lattice_info = read_contcar(zjw)

Ni_site_number = find_the_max_site(atom_array, atom_list)
# 注意 numpy原子序号从0开始  而xsd文件中的是从1开始,  数值差1
# 得到吸附位点的序号(==>numpy)

site_ID = Ni_site_number   # need to give the Ni site (ads site)
print site_ID
length = atom_array.shape[0]
# for i in extract_local_structure(atom_array, atom_list, site_ID):
#     print i
# 顺便算一下库伦矩阵
coulomb_matrix = np.zeros((length, length))
for i in range(length):
    for j in range(length):
        coulomb_matrix[i][j] = coulomb_matrix_calculate(
            i, j, atom_list, atom_array, lattice_info)


locals = extract_local_structure(atom_array, atom_list, site_ID, lattice_info)
'''
格式化输出 局部结构的信息:
        原子名称,  原子序号, 距离Ni Site多少, 坐标(相对), 键角(M - Ni - Z_axis)
'''


local_infomation = local_structure_cal(
    locals, site_ID, atom_array, lattice_info)

print local_infomation

with open('./data.txt', 'w') as fuck:
    fuck.write('local structure data information\n')
    for i in local_infomation:
        s = '    '.join(i) + '\n'
        fuck.write(s)
