#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jwz@ecust on 12/29/16
import numpy as np
import os
import re


class RadioDisFunc(object):

    def __init__(self, localstructure, Rc=6, Rs=6, yita=0.5, eptheno=0.5, lamta=0.5):
        self.total = len(localstructure)
        self.coordinates = np.zeros((self.total, 3))
        for i in range(self.total):
            self.coordinates[i] = localstructure[i][0]
        self.atoms = [_[1] for _ in localstructure]

    @staticmethod
    def fc(Rij, Rc=6.0):
        if Rij <= Rc:
            return 0.5*np.cos(np.pi*Rij/Rc) + 1
        else:
            return 0

    def g1(self, Rc=6.0):
        dis = [np.linalg.norm(self.coordinates[i]-self.coordinates[0]) for i in range(1, self.total)]
        tem = [self.fc(rij) for rij in dis]
        return sum(tem)


    def g2(self, yita=0.5, Rs=6.0):
        dis = [np.linalg.norm(self.coordinates[i]-self.coordinates[0]) for i in range(1, self.total)]
        tem = [self.fc(rij)*np.exp(-yita*(rij-Rs)**2) for rij in dis]
        return sum(tem)

    def g3(self):
        g3 = 0.0
        for i in range(1, self.total):
            fcik = 0.0
            fcjk = 0.0
            rij = self.coordinates[i] - self.coordinates[0]
            rij_n = np.linalg.norm(rij)
            for j in range(i+1, self.total):
                rik = self.coordinates[j] - self.coordinates[0]
                rjk = self.coordinates[i] - self.coordinates[j]
                rik_n = np.linalg.norm(rik)
                rjk_n = np.linalg.norm(rjk)
                fcik += self.fc(rik_n)
                fcjk += self.fc(rjk_n)
            g3 += self.fc(rij_n)*(fcik + fcjk)
        return g3

    def g4(self, yita=0.5, eptheno=0.5):
        g4 = 0.0
        for i in range(1, self.total):
            rij = self.coordinates[i] - self.coordinates[0]
            rij_n = np.linalg.norm(rij)
            for j in range(i+1, self.total):
                rik = self.coordinates[j] - self.coordinates[0]
                rik_n = np.linalg.norm(rij)
                rjk = self.coordinates[i] - self.coordinates[j]
                rjk_n = np.linalg.norm(rij)
                if self.cosijk(rij, rik) >= 0:
                    lamta = +1
                else:
                    lamta = -1
                g4 = g4 + (1 + lamta*self.cosijk(rij, rik))**eptheno*np.exp(-yita*(rij_n**2+rik_n**2+rjk_n**2))*self.fc\
                    (rij_n)*self.fc(rik_n)*self.fc(rjk_n)
        g4 = 2**(1-eptheno)*g4
        return g4

    def g5(self, yita=0.5, eptheno=0.5):
        g5 = 0.0
        for i in range(1, self.total):
            rij = self.coordinates[i] - self.coordinates[0]
            rij_n = np.linalg.norm(rij)
            for j in range(i+1, self.total):
                rik = self.coordinates[j] - self.coordinates[0]
                rik_n = np.linalg.norm(rij)
                if self.cosijk(rij, rik) >= 0:
                    lamta = +1
                else:
                    lamta = -1
                g5 = g5 + (1 + lamta*self.cosijk(rij, rik))**eptheno*np.exp(-yita*(rij_n**2+rik_n**2))*self.fc(rij_n)*\
                          self.fc(rik_n)
        g5 = 2**(1-eptheno)*g5
        return g5

    def atom_ratio(self):
        atom_type = set(self.atoms)
        atom_dict = {}
        for i in atom_type:
            atom_dict[i] = self.atoms.count(i)
        return 1.0*atom_dict['Ni']/atom_dict['P']

    def cosijk(self, Rij, Rik):
        return np.dot(Rij, Rik)/(np.linalg.norm(Rij)*np.linalg.norm(Rik))


def get_final_energy(oszicar_path):
    '''
    给定 OSZICAR 文件的路径
    通过正则获取能量数据
    并返回最后一步的能量
    '''
    with open(oszicar_path) as fuck:
        return float(re.findall('E0= (.+?\+\d{2})', fuck.read())[-1])


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

        Ni_list = []
        for i in range(total_number):
            if atom_array[i] == 'Ni':
                Ni_list.append(i)
        Site = Ni_list[coordinate[Ni_list].argmax(axis=0)[2]]
        local_structure = [(i[0][0], i[0][1], i[1]) for i in zip(zip(coordinate, atom_array), range(total_number))]

        # local_structure = sorted(local_structure, key=lambda x: np.linalg.norm(x[0] - coordinate[Site]))[:11]
        local_structure = sorted(local_structure, key=lambda x: np.linalg.norm(x[0] - coordinate[Site]))

        # 包含了Site
        return local_structure


# adsorption energy
unad_oszicar = '/Volumes/WD/data/NiP_data/surface/oszicar'
ad_oszicar = '/Volumes/WD/data/NiP_data/surface_and_CO/oszicar'
co_energy = -14.7714764


# contcar files
contcar = '/Volumes/WD/data/NiP_data/surface/contcar'
contfiles = os.listdir(contcar)
f = open('./rdf.txt', 'w')
for i in contfiles:
    cont_path = contcar + '/' + i
    number = cont_path.split('_')[-1]
    cont_path = contcar+'/CONTCAR_slab_' + str(number)
    unad_path = unad_oszicar + '/OSZICAR_' + str(number)
    ad_path = ad_oszicar + '/OSZICAR_' + str(number)
    ads = get_final_energy(ad_path) - get_final_energy(unad_path) - co_energy
    # energy = get_final_energy(unad_path)
    ccc = readcontcar(cont_path)
    info = RadioDisFunc(ccc)
    if -2.0 < ads < -0.8:
        f.write(str(info.g1()) + ' ' + str(info.g2()) + ' ' + str(info.g3()) + ' ' + str(info.g4()) + ' ' + \
                str(info.g5()) + ' ' + str(ads) + '\n')
