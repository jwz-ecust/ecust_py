from ase import Atoms
from ase.build import fcc111
from ase.visualize import view
d = 1.10
molecule = Atoms('2O',positions=[(0.0,0.0,0.0),(0.0,0.0,d)])
slab = fcc111('Ag',size=(4,4,6),vacuum=20.0)
view(molecule)
view(slab)