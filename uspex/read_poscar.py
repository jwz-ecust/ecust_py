import numpy as np


def read_poscar(poscat_file_path):
    with open(poscat_file_path) as file_poscar:
        title = file_poscar.readline().strip()
        # get the first line, usually called name
        factor = float(file_poscar.readline().strip())
        lattice = np.zeros((3, 3))
        for i in range(3):
            tem_line = file_poscar.readline().strip().split(' ')
            tem_line = [j for j in tem_line if j]
            lattice[i, :] = np.array(tem_line, dtype=float)
        lattice = lattice * factor
        # get the lattice parameters
        atom_type = file_poscar.readline().strip().split('    ')
        # return a list containing Atom type
        atom_number = file_poscar.readline().strip().split('    ')
        atom = {}
        for i in range(len(atom_type)):
            atom[atom_type[i]] = int(atom_number[i])
        total_number = sum(atom.values())
        coordinate = np.zeros((total_number, 4))
        for i in range(2):
            _ = file_poscar.readline()
        for i in range(total_number):
            temp = file_poscar.readline()
            tt = temp.strip().split(' ')
            tt = [_ for _ in tt if _]
            coordinate[i, 0:3] = np.array(tt[0:3], dtype=float)
            if 'T' in tt:
                # 1 means T,  0 means F
                coordinate[i, 3] = 1
            else:
                coordinate[i, 3] = 0

    return lattice, atom, coordinate


path = '/Users/zhangjiawei/Code/zjw/uspex/POSCAR'
lattice, atom, coordinate = read_poscar(path)

print lattice
print atom
print coordinate
