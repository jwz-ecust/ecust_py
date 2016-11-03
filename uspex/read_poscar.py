import numpy as np


def read_poscar(poscat_file_path):
    with open(poscat_file_path) as file_poscar:
        title = file_poscar.readline().strip()  # useless

        # get the first line, usually called name
        factor = float(file_poscar.readline().strip())
        lattice = np.zeros((3, 3))
        for i in range(3):
            tem_line = file_poscar.readline().strip().split(' ')
            tem_line = filter_blank(tem_line)
            lattice[i, :] = np.array(tem_line, dtype=float)
        lattice = lattice * factor

        # get the lattice parameters
        atom_type = file_poscar.readline().strip().split('    ')
        # return a list containing Atom type
        atom_number = file_poscar.readline().strip().split('    ')
        atom = {}

        # return a dictoion key=atom type, value=atom number
        for i in range(len(atom_type)):
            atom[atom_type[i]] = int(atom_number[i])
        total_number = sum(atom.values())
        coordinate = np.zeros((total_number, 4))

        # jump two lines (null)
        for i in range(2):
            _ = file_poscar.readline()

        # read coordinate data
        # coordinate(x, y, z)  (fix or unfix)
        for i in range(total_number):
            temp = file_poscar.readline()
            tt = temp.strip().split(' ')
            tt = filter_blank(tt)
            coordinate[i, 0:3] = np.array(tt[0:3], dtype=float)
            if 'T' in tt:
                # 1 means T,  0 means F
                coordinate[i, -1] = 1
            else:
                coordinate[i, -1] = 0
    return lattice, atom, coordinate


def filter_blank(line):
    '''
    filter blank in  a given list
    '''
    return [_ for _ in line if _]


path = '/Users/zhangjiawei/Code/zjw/uspex/POSCAR'
lattice, atom, coordinate = read_poscar(path)

print lattice
print atom
print coordinate
