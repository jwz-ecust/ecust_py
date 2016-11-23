# -*- coding: utf-8 -*-
import os
import numpy as np

'''
用于读取CONTCAR
添加C O 坐标
生成新的POSCAR
'''

# cwd = os.getcwd()
# contcar = os.path.join(cwd, 'CONTCAR')
# poscar = os.path.join(cwd, 'POSCAR')


def add_CO(contcar, poscar):
    if os.path.exists(contcar):
        with open(contcar, 'r') as ff:
            content = ff.readlines()
            lattice = np.zeros((3, 3))
            # 提取 晶胞参数
            for i in range(3):
                lattice[i] = np.array(
                    [_ for _ in content[i + 2].strip().split(' ') if _], dtype=np.float)
            # 获取原子种类和数目
            atom_number = content[6].strip().split(' ' * 4)
            atom_type = content[5].strip().split(' ' * 4)
            atom = dict(zip(atom_type, atom_number))
            content[5] = '  C    O  ' + content[5]
            content[6] = '  1    1 ' + content[6]
            t_number = sum([int(i) for i in atom.values()])
            Ni_number = int(atom['Ni'])
            xyz_array = np.zeros((t_number, 3))
            for i in range(9 + int(atom['P']), 9 + t_number):
                _xyz = [_ for _ in content[i].strip().split(' ') if _][0:3]
                xyz_array[i - 9, :] = np.array(_xyz, dtype=np.float)
            # 找到吸附位点
            ads_site = xyz_array[:, 2].argmax()
            lattice_c = lattice.diagonal()[2]
            # 生成C O原子的坐标
            bond_dis_c = 1.888    # C-Ni bond distence
            bond_dis_o = 3.000    # C-Ni+ CO bond dis
            C_site = xyz_array[ads_site] + \
                np.array([0.0, 0.0, bond_dis_c / lattice_c])
            O_site = xyz_array[ads_site] + \
                np.array([0.0, 0.0, bond_dis_o / lattice_c])
            C_xyz = ' ' + ' '.join([str('%.16f' % i).rjust(19)
                                    for i in C_site]) + '   T   T   T\n'
            O_xyz = ' ' + ' '.join([str('%.16f' % i).rjust(19)
                                    for i in O_site]) + '   T   T   T\n'
            # 生成新的POSAR, 并写入文件
            new_content = content[0:9] + [C_xyz, O_xyz] + content[9:]
            for i in new_content:
                print i
            with open(poscar, 'w') as ttt:
                ttt.writelines(new_content)


contcar = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/CONTCAR'
poscar = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/POSCAR'
add_CO(contcar, poscar)

# rootdir = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/gathered_contcar'
#
# list_dirs = os.listdir(rootdir)
#
# for i in list_dirs:
#     full_path = os.path.join(rootdir, i)
#     if os.path.isdir(full_path):
#         contcar = os.path.join(full_path, 'CONTCAR')
#         poscar = os.path.join(full_path, 'POSCAR')
#         add_CO(contcar, poscar)
