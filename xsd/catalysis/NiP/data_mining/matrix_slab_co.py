import os
import numpy as np
import re


def read_contcar(contcar_path):

    with open(contcar_path, 'r') as f:
        info = f.readlines()
        _lattice = info[2:5]
        lattice = np.zeros((3, 3), dtype=np.float)
        for i in range(3):
            lattice[i] = [float(_)
                          for _ in _lattice[i].strip().split(' ') if _]

        atom_type = info[5].strip().split("    ")
        atom_number = [int(_) for _ in info[6].strip().split("    ")]
        total_number = sum(atom_number)
        atom = dict(zip(atom_type, atom_number))
        atom_array = []
        for i in atom_type:
            atom_array.extend([i] * atom[i])

        coordinate = np.zeros((total_number, 3))

        _coordinates = info[9: 9 + total_number]
        for i in range(total_number):
            temp = [_ for _ in _coordinates[i].strip().split(' ') if _][0:3]
            coordinate[i] = [float(_) for _ in temp]

    return coordinate, atom_array, lattice


def dis_calculate(i, j, atom_array, lattice_info):
    '''
    this is used to calculate the distence between two atoms
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
    length = atom_array.shape[0]
    cou_matrix = np.zeros((length, length))
    for i in range(length):
        for j in range(length):
            cou_matrix[i][j] = coulomb_matrix_calculate(
                i, j, atom_list, atom_array, lattice_info)
    return cou_matrix


def get_final_energy(oszicar_path):

    with open(oszicar_path) as fuck:
        return float(re.findall('E0= (.+?\+\d{2})', fuck.read())[-1])


# co_path = "/Volumes/WD/data/NiP_data/surface_and_CO/contcar/CONTCAR_CO_1"
# slab_path = "/Volumes/WD/data/NiP_data/surface/contcar/CONTCAR_slab_1"
# slab_array, slab_list, lattice_slab = read_contcar(slab_path)
# co_array, co_list, lattice_co = read_contcar(co_path)
# slab_matrix = _get_coulomb_matrix(slab_list, slab_array, lattice_slab)
# co_matrix = _get_coulomb_matrix(co_list, co_array, lattice_co)
# a, _ = np.linalg.eig(slab_matrix)
# b, _g = np.linalg.eig(co_matrix)
# print a - b

energy_of_CO = -14.7714764
path = "/Volumes/WD/data/NiP_data/"
fuck = open('./zhangjiawei_data.txt', 'w')
for num in range(1, 111):
    contcar_slab = path + "surface/contcar/CONTCAR_slab_{}".format(num)
    contcar_co_path = path + "surface_and_CO/contcar/CONTCAR_CO_{}".format(num)

    slab_array, slab_list, lattice_slab = read_contcar(contcar_slab)
    co_array, co_list, lattice_co = read_contcar(contcar_co_path)
    new_co_array = co_array[2:, :]
    new_co_list = co_list[2:]

    slab_matrix = _get_coulomb_matrix(slab_list, slab_array, lattice_slab)
    co_matrix = _get_coulomb_matrix(new_co_list, new_co_array, lattice_co)
    slab_eig, _ = np.linalg.eig(slab_matrix)
    co_eig, _ = np.linalg.eig(co_matrix)
    eig_difference = slab_eig
    #  - co_eig

    surface_path = path + "surface/oszicar/OSZICAR_{}".format(num)
    co_and_surface_path = path + \
        "surface_and_CO/oszicar/OSZICAR_{}".format(num)
    energy_of_surface = get_final_energy(surface_path)
    energy_of_CO_and_surface = get_final_energy(co_and_surface_path)
    energy_of_adsorption = energy_of_CO_and_surface - energy_of_surface - energy_of_CO
    fuck.write(' '.join([str(i) for i in eig_difference]) +
               ' ' + str(energy_of_adsorption) + '\n')


fuck.close()
