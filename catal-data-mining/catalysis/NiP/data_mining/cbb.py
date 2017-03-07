# -*- coding: utf-8 -*-
# author: jwz-ecust
# mail: jwz_ecust@mail.ecust.edu.cn

import xml.etree.cElementTree as ET
import os
import numpy as np
import re


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


def get_final_energy(oszicar_path):
    '''
    给定 OSZICAR 文件的路径
    通过正则获取能量数据
    并返回最后一步的能量
    '''
    with open(oszicar_path) as fuck:
        return float(re.findall('E0= (.+?\+\d{2})', fuck.read())[-1])


def read_bader(bader_path):
    bader = []
    with open(bader_path) as bd:
        content = bd.readlines()
        for i in content[2:-4]:
            bader.append(i.strip().split(" " * 5)[4])
    return bader


#  get all data
def get_data():
    energy_of_CO = -14.7714764
    path = "/Volumes/WD/data/NiP_data/"
    with open('./coulomb.txt', 'w') as fuck:
        for num in range(1, 111):
            bader_path = path + "surface/bader/ACF_{}.dat".format(num)
            contcar = path + "surface/contcar/CONTCAR_slab_{}".format(num)
            surface_path = path + "surface/oszicar/OSZICAR_{}".format(num)
            co_and_surface_path = path + \
                "surface_and_CO/oszicar/OSZICAR_{}".format(num)
            energy_of_surface = get_final_energy(surface_path)
            energy_of_CO_and_surface = get_final_energy(co_and_surface_path)
            energy_of_adsorption = energy_of_CO_and_surface - energy_of_surface - energy_of_CO

            atom_array, atom_list, lattice_info = read_contcar(contcar)
            site_ID = find_the_max_site(atom_array, atom_list)
            length = atom_array[0]

            locals = extract_local_structure(
                atom_array, atom_list, site_ID, lattice_info)
            local_infomation = local_structure_cal(
                locals, site_ID, atom_array, lattice_info)

            # 获取局部结构的库伦矩阵
            charge_info = {'C': 4.0, 'O': 6.0, 'P': 5.0, 'Ni': 10.0}
            # print len(local_matrix_prepare)
            # 获取bader 列表
            bader = read_bader(bader_path)

            ads_site = atom_array[site_ID]
            local_matrix = []

            for i in range(10):
                atom_number = int(local_infomation[i][1])
                dis = local_infomation[i][2]
                #atom_2 = 'Ni'
                local_matrix.append(
                    float(bader[atom_number]) * float(bader[site_ID]) / (float(dis)**2))
            local_matrix.append(energy_of_adsorption)

            fuck.write(' '.join([str(_) for _ in local_matrix]) + '\n')

            # fuck.write("Number: " + str(num) + '\n')
            # fuck.write("CO Adsorption Energy: " +
            #            str(energy_of_adsorption) + '\n')
            # for zzz in local_infomation:
            #     fuck.write('\t'.join(zzz) + '\n')
            # fuck.write('\n\n\n')

get_data()


'''
[['P', '4', '2.24590162186', '0.554157217815', '0.298572318951', '0.366982911299', '151.90541729', '99.7450722323'], ['P', '0', '2.27117855945', '0.792101481684', '0.629077925573', '0.45215429285', '138.047707674', '88.9721968434'], ['Ni', '14', '2.85224244144', '0.9169475028', '0.519923728992', '0.349488612883', '153.858928226', '101.675522767'], ['Ni', '15', '3.39176270569', '0.279106614609', '0.482372246793', '0.420991499626', '143.776141306', '93.1034035534'], ['Ni', '25', '3.63757073634', '0.587745443076', '0.809879583216', '0.378250268377', '150.453993379', '98.438250089'], ['P', '1', '4.03753251757', '0.118871141074', '0.145476765681', '0.483421266236', '131.928445882', '84.803850225'], ['Ni', '20', '4.10835189777', '0.456089829314', '0.0359280135099', '0.281521535392', '157.782619675', '107.956588701'], ['Ni', '22', '4.34919801556', '0.578335324851', '0.522443901902', '0.271208107602', '157.907003071', '108.743157236'], ['P', '5', '4.45788220366', '0.0673769801427', '0.148560800667', '0.384276910284', '149.61941014', '97.7201579506'], ['P', '11', '4.75401908466', '0.803851880123', '0.871503174942', '0.295808664744', '157.425232414', '106.796956292']]

'''
