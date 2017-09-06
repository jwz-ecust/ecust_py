from ase import Atoms
from ase.visualize import view
import numpy as np


# read contcar
def readcontcar(contcarpath):
    with open(contcarpath, 'r') as f:
        info = f.readlines()
        lattice = info[2:5]
        lattice = [[float(_) for _ in i.strip().split(" ") if _] for i in lattice]
        lattice = np.array(lattice)
        abc = ((lattice**2).sum(axis=1))**0.5
        atom = info[5 : 7]
        atom = [[_ for _ in i.strip().split("    ")] for i in atom]
        total_number = sum([int(i) for i in atom[1]])

        atom_array = []
        for i, j in zip(atom[0], atom[1]):
            atom_array += [i] * int(j)

        _coordinates = info[9: 9 + total_number]
        coordinate = np.array([[t for t in i.strip().split(" ") if t][:3] \
            for i in _coordinates], dtype=float)
        coordinate = coordinate * abc
        return atom_array, coordinate


cont = "/Users/zjw/Documents/code/zjw/multi_thread/6_CONTCAR"
atom_array, coordinate = readcontcar(cont)

atomlists = "".join(atom_array)
coordinates = coordinate.tolist()
molecule = Atoms(atomlists, positions=coordinates)

view(molecule)
