from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units
d = 1.10
molecule = Atoms('2N',positions=[(0., 0., 0.), (0., 0., d)])
molecule.set_calculator(EMT())
dyn = VelocityVerlet(molecule, dt=1.0*units.fs)
for i in range(20):
    pot = molecule.get_potential_energy()
    kin = molecule.get_kinetic_energy()
    print '%2d: %.5f eV, %.5f eV, %.5f eV' % (i, pot + kin, pot, kin)
    dyn.run(steps=30)