# -*- coding: utf-8 -*-
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


def dis_calculate(i, j, atom_array, lattice_info):
    '''
    this is used to calculate the distence between two atoms
    相对坐标需要转化为绝对坐标
    '''
    abc = lattice_info.diagonal()
    i_ads_coor = atom_array[i].dot(abc)
    j_ads_coor = atom_array[j].dot(abc)
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
    local_dis = []
    ads_site = atom_array[site_ID]
    for i in range(2, len(atom_list)):
        if i == site_ID:
            local_dis.append((atom_list[i], i, 0.0, atom_array[i]))
        else:
            local_dis.append((atom_list[i], i, dis_calculate(
                i, site_ID, atom_array, lattice_info), atom_array[i]))
    return sorted(local_dis, key=lambda x: x[2])[1:n + 1]


def bond_angle_cal(i_array, j_array):
    # 角度计算, 余弦,  反三角函数
    dot_product = i_array.dot(j_array)
    i = np.linalg.norm(i_array)
    j = np.linalg.norm(j_array)
    return np.arccos(dot_product / (i * j)) * 180 / np.pi


def local_structure_cal(locals, ads_ID, site_ID, atom_array, lattice_info):
    '''
    计算局部结构的信息
    返回 键长, 键角
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    考虑与吸附 Site(Ni) 最近的10个原子 (这里先考虑10个原子)
        1. distance  finished
        2. 夹角 (考虑 OC-Ni-M 之间的夹角) finished
        3. 原子的电负性 (考虑中) ===> 包含在 库伦矩阵中???
        4. d-band center (未考虑)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    '''

    ads_bond = atom_array[ads_ID] - atom_array[site_ID]
    info_local_structure = []
    for i in locals:
        sub_bond = i[-1] - atom_array[site_ID]
        angle = bond_angle_cal(ads_bond, sub_bond)
        info_list = list(i)
        info_list.append(angle)
        info_local_structure.append(info_list)
    return info_local_structure


path = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP-001-adsorb-co.xsd'
atom_array, atom_list, lattice_info = read_xsd(path)
site_ID = 56
ads_ID = 1
length = atom_array.shape[0]
# for i in extract_local_structure(atom_array, atom_list, site_ID):
#     print i
# 顺便算一下库伦矩阵
coulomb_matrix = np.zeros((length, length))
for i in range(length):
    for j in range(length):
        coulomb_matrix[i][j] = coulomb_matrix_calculate(
            i, j, atom_list, atom_array, lattice_info)

# print coulomb_matrix
# 对库伦矩阵 SVD 分解一下
# _, sig, _ = np.linalg.svd(coulomb_matrix)
# print sig


locals = extract_local_structure(atom_array, atom_list, site_ID, lattice_info)

#  格式化输出 局部结构的信息:    原子名称,  原子序号, 距离Ni Site多少, 坐标(相对), 键角(M-Ni-C)comcom
for i in local_structure_cal(locals, ads_ID, site_ID, atom_array, lattice_info):
    # print i
    print "The atom name is {}, the number is {}, the distence from Ni is {}, the coordiante is {} and the C-Ni-M angle is {}".format(*i)
