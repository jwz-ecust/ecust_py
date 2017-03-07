#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 17/1/6
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 12/29/16
import numpy as np
import matplotlib.pyplot as plt
import os
import re



def get_final_energy(oszicar_path):
    '''
    给定 OSZICAR 文件的路径
    通过正则获取能量数据
    并返回最后一步的能量
    '''
    with open(oszicar_path, 'r') as fuck:
        return float(re.findall('E0= (.+?\+\d{2})', fuck.read())[-1])


def get_feimi_energy(outcar_path):
    with open(outcar_path, 'r') as fuck:
        return re.findall('E-fermi :   (\d\.\d{4})', fuck.read())[-1]


class galphabeta(object):
    def __init__(self, coordinate, atoms, site, n=28):
        '''
        n 代表 rn的个数
        '''
        self.total = len(coordinate)
        self.coordinates = coordinate
        self.atoms = atoms
        self.site = site
        self.Ps = coordinates[np.array([i == 'P' for i in atoms])]
        self.Nis = coordinates[np.array([i == 'Ni' for i in atoms])]
        self.r = np.linspace(1., 10., n)
        self.dr = (10. - 1.)/(n-1)

    def theta(self, delta):
        if delta > 0:
            return 1
        else:
            return 0


    def g(self, distance):
        NNi = len(self.Nis)
        V = np.pi*4.0/3*distance**3
        g = 0.0
        for i in self.Nis:
            for j in self.Ps:
                dis = np.linalg.norm(i-j)
                g += self.theta(dis - distance)*self.theta(distance + self.dr - dis)
        g = g/(V*NNi)
        return g

    def g_r(self):
        rrr = []
        for i in self.r:
            rrr.append(self.g(i))
        return rrr


def readcontcar(contcar_path):

    # Target: 需要读取 原子种类, 原子笛卡尔坐标
    # atom: 字典  {'P':14, 'Ni':14}
    # atom_array: ['P', 'P', ...., 'Ni',...,'Ni']
    # coordinates: 28x3 numpy array

    with open(contcar_path, 'r') as ffuck:
        info = ffuck.readlines()
        # 获取晶胞参数信息
        _lattice = info[2:5]
        lattice = np.zeros((3, 3), dtype=np.float)
        for i in range(3):
            lattice[i] = [float(_) for _ in _lattice[i].strip().split(' ') if _]
        lattice = np.array(lattice, dtype=float)
        abc = np.sqrt(np.sum(np.square(lattice), axis=1))
        # 获取元素种类, 数目信息
        atom_type = info[5].strip().split("    ")
        atom_number = [int(_) for _ in info[6].strip().split("    ")]
        total_number = sum(atom_number)
        atom = dict(zip(atom_type, atom_number))
        atom_array = [atom_type[0]] * atom[atom_type[0]] + \
            [atom_type[1]] * atom[atom_type[1]]
        # 获取坐标
        coordinate = np.zeros((total_number, 3))
        _coordinates = info[9: 9 + total_number]
        for i in range(total_number):
            temp = [_ for _ in _coordinates[i].strip().split(' ') if _][0:3]
            coordinate[i] = [float(_) for _ in temp]
        coordinate = coordinate * abc.T

        atom_bool = np.array([ i == 'Ni' for i in atom_array], dtype=bool)
        site = np.where(coordinate == max(coordinate[atom_bool][:, 2]))[0][0]

        return coordinate, atom_array, site


# contcar files
# contcar = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP/prdf/contcar'
# coordinates, atoms, site = readcontcar(contcar)
# zjw = galphabeta(coordinates, atoms, site)
# gr = zjw.g_r()
# plt.plot(zjw.r, gr)
#
# plt.show()

contcar = '/Volumes/WD/data/NiP_data/surface/contcar'
contfiles = os.listdir(contcar)



# adsorption energy
unad_oszicar = '/Volumes/WD/data/NiP_data/surface/oszicar'
ad_oszicar = '/Volumes/WD/data/NiP_data/surface_and_CO/oszicar'
outcar = '/Volumes/WD/data/NiP_data/surface/outcar'
co_energy = -14.7714764
f = open('./gab.txt', 'w')

for i in contfiles:
    cont_path = contcar + '/' + i
    coordinates, atoms, site = readcontcar(cont_path)
    zjw = galphabeta(coordinates, atoms, site)
    gr = zjw.g_r()
    number = cont_path.split('_')[-1]
    out_path = outcar + '/OUTCAR_' + str(number)
    Efermi = get_feimi_energy(out_path)


    unad_path = unad_oszicar + '/OSZICAR_' + str(number)
    Eslab = get_final_energy(unad_path)
    # ad_path = ad_oszicar + '/OSZICAR_' + str(number)
    # ads = get_final_energy(ad_path) - get_final_energy(unad_path) - co_energy
    f.write(' '.join([str(_) for _ in gr]) + ' ' + str(Eslab) + '\n')

#     plt.plot(zjw.r, gr)
# plt.show()




'''
['Ni', 'P', 'P', 'Ni', 'Ni', 'Ni', 'P', 'P', 'P', 'P', 'Ni', 'Ni', 'Ni', 'Ni', 'P', 'P', 'Ni', 'Ni', 'P', 'Ni', 'P', 'Ni', 'Ni', 'P', 'P', 'Ni', 'P', 'P']
'''
