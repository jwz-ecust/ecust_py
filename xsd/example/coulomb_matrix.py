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


def dis_cal(a, b):
    '''
    this is used to calculate the distence between two atoms
    '''
    return np.sqrt(sum((a - b)**2))


def coulomb_effect_cal(i, j):
    '''
    this is used to calculate the coulomb effect
    '''
    charge_info = {'P': 5.0, 'Ni': 10.0}   # charge

    if i == j:
        effect = 0.5 * charge_info[atom_list[i]]**2.4
    else:
        effect = charge_info[atom_list[
            i]] * charge_info[atom_list[j]] / dis_cal(atom_array[i], atom_array[j])
    return effect


path = '/Users/zhangjiawei/Code/zjw/xsd/example/NiP.xsd'
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

#  获取表面一个Ni site 的坐标
zjw = atom_array[28:][:, 2]
a = zjw.argmax()
number = a + 28
# 计算其他原子到Ni的距离, 库伦作用


# 计算库伦矩阵
length = atom_array.shape[0]
atom_matix = np.zeros((length, length))
for i in range(length):
    for j in range(length):
        atom_matix[i][j] = coulomb_effect_cal(i, j)

# SVD 奇异值分解一下
U, Sigma, VT = np.linalg.svd(atom_matix)

# print U
# print Sigma
# print VT
