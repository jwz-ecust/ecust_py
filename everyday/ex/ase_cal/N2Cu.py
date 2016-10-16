from ase. import fcc111
from ase.visualize import view
slab = fcc111('Cu', size=(4, 4, 2), vacuum=10.0)
view(slab)