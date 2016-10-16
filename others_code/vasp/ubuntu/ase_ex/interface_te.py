from ase.io import read
import numpy as np
from ase.build import fcc111
from ase.visualize import view
W = read('WL.traj')

cellW = W.get_cell()
slab = fcc111('Ni',size=[2,4,3],a=0.35,orthogonal=True)
cell = slab.get_cell()
W.set_cell([[cellW[1, 1], 0, 0], [0, cellW[0, 0], 0], cellW[2]], scale_atoms=False)
W.rotate('z',np.pi/2,center=(0,0,0))
W.wrap()

cell1 = np.array([cell[0], cell[1], cellW[2]])
W.set_cell(cell1, scale_atoms=True)
p = slab.get_positions()
W.center(vacuum=p[:, 2].max() + 1.5, axis=2)
interface = slab.copy()
interface.extend(W)
interface.center(vacuum=6, axis=2)
view(interface)