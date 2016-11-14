# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import os
import numpy as np

'''
库伦矩阵:
Z_i: 代表i原子的核电荷数 (考虑价电子数???)

C_ij = {0.5Z_i**2.4: i=j, Z_i*Z_j/(dis_between i and j): i!=j }

NiP 001 surface    Ni: 28  P: 28
'''


path = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP.xsd'
root = ET.ElementTree(file=path)


atom_list = []
coordiante_list = []
# get the atom coordiantes  and type
for element in root.iter():
    # print "Tag:%s\nAttrib:%s\nText:%s" % (element.tag, element.attrib,
    #                                       element.text)
    if element.attrib.has_key('XYZ'):
        atom = element.attrib['Components']
        coordiante = element.attrib['XYZ'].split(',')
        atom_list.append(atom)
        coordiante_list.append(coordiante)

atom_array = np.array(coordiante_list, dtype=np.float)
length = atom_array.shape[0]


def dis_cal(i, j):
    '''
    this is used to calculate the distence between two atoms
    '''
    square = np.square(atom_array[i] - atom_array[j])
    return np.sqrt(square.sum())
    # 计算距离的话, 应该晶胞参数 a, b, c


def coulomb_effect_cal(i, j):
    '''
    this is used to calculate the coulomb effect
    '''
    charge_info = {'P': 5.0, 'Ni': 10.0}   # charge

    if i == j:
        effect = 0.5 * charge_info[atom_list[i]]**2.4
    else:
        effect = charge_info[atom_list[
            i]] * charge_info[atom_list[j]] / dis_cal(i, j)
    return effect


#  获取表面一个Ni site 的坐标
zjw = atom_array[28:][:, 2]
a = zjw.argmax()
number = a + 28

# 计算其他原子到Ni的距离, 库伦作用
# [
#   ['columb effect', 'dis']
#         ....
#         ....
#         ....
#   ['columb effect', 'dis']
#]

dis_and_coulomb_array = np.zeros((length, 2))

for i in range(0, length):
    if i == number:
        dis_and_coulomb_array[i] = [0.0, 0.0]
    else:
        dis_and_coulomb_array[i][0] = coulomb_effect_cal(number, i)
        dis_and_coulomb_array[i][1] = dis_cal(number, i)

# print dis_and_coulomb_array


##########################################################################
'''
================================================================================
考虑与吸附 Site(Ni) 最近的10个原子 (这里先考虑10个原子)
    1. distance
    2. 夹角 (考虑 OC-Ni-M 之间的夹角)
    3. 原子的电负性
    4. d-band center
================================================================================
'''


def extract_local_character_N(atom_array, atom_list, number):
    '''
    需要输入原子坐标和原子种类列表 以及 吸附site的序号
    返回 距离吸附site Ni 最近的10个原子的列表 组成 (atom_type, atom_number, distance, atom_coordinate)
    '''
    local_dis = []
    ads_site = atom_array[number]
    for i in range(len(atom_array)):
        if i == number:
            local_dis.append((atom_list[i], i, 0.0, atom_array[i]))
        else:
            local_dis.append(
                (atom_list[i], i, dis_cal(i, number), atom_array[i]))
    return sorted(local_dis, key=lambda x: x[2])[1:11]   # 返回距离吸附site最近的10原子


for i in extract_local_character_N(atom_array, atom_list, number):
    print i


##########################################################################

# 计算库伦矩阵
atom_matix = np.zeros((length, length))
for i in range(length):
    for j in range(length):
        atom_matix[i][j] = coulomb_effect_cal(i, j)

# SVD 奇异值分解一下
U, Sigma, VT = np.linalg.svd(atom_matix)

# print U
# print Sigma
# print VT
