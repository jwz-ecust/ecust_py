# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
# Copyright (c) 2008-2013 Janne Blomqvist

# This source code file is subject to the terms of the MIT (Expat)
# License. See the file LICENSE for details.

"""Module for doing stuff with density-of-states."""

import matplotlib.pyplot as plt
import numpy as np
import sys
import warnings

class LDOS(object):
    """Class for representing a set of local DOS.
    
    DOS data is stored in the instance variable self.dos, which is a 3D 
    ndarray, as follows:
    1st dim: Which atom.
    2nd dim: Selects the DOS grid point.
    3rd dim: 0 is the energy, 1-3 s, p, d DOS.
        
    """

    def __init__(self, doscar="DOSCAR", efermi=0.0):
        """Initialize LDOS."""
        warnings.warn('vasputil.dos.LDOS is deprecated, please use \
 ase.calculators.vasp.VaspDos instead, which is an improved version if this \
 class', DeprecationWarning)
        self._efermi = 0.0
        self.read_doscar(doscar)
        self.efermi = efermi

    def read_doscar(self, fname="DOSCAR"):
        """Read a VASP DOSCAR file."""
        f = open(fname)
        natoms = int(f.readline().split()[0])
        [f.readline() for nn in range(4)]  # Skip next 4 lines.
        dos = []
        for na in xrange(natoms + 1):
            try:
                line = f.readline()
                if line == "":
                    raise Exception
            except Exception:
                errstr = "Failed reading " + str(na) + ":th DOS block, probably " \
                        + "this DOSCAR is from some old version of VASP that " \
                        + "doesn't " \
                        + "first produce a block with integrated DOS. Inserting " \
                        + "empty 0:th block."
                sys.stderr.write(errstr)
                dos.insert(0, np.zeros((ndos, dos[1].shape[1])))
                continue
            try:
                ndos = int(line.split()[2])
            except Exception:
                print "Error, line is: " + line + "ENDLINE"
            line = f.readline().split()
            cdos = np.zeros((ndos, len(line)))
            cdos[0] = np.array(line)
            for nd in xrange(1, ndos):
                line = f.readline().split()
                cdos[nd] = np.array(line)
            dos.append(cdos)
        f.close()
        if dos[0].shape != dos[1].shape:
            dos0 = np.zeros(dos[1].shape)
            dos0[:,:dos[0].shape[1]] = dos[0]
            dos[0] = dos0
        self.dos = np.array(dos)

    def _set_efermi(self, efermi):
        """Set the Fermi level."""
        if self._efermi != 0.0:
            self.dos[:,:,0] = self.dos[:,:,0] + self._efermi
        self._efermi = efermi
        self.dos[:,:,0] = self.dos[:,:,0] - efermi

    def _get_efermi(self):
        return self._efermi

    def _del_efermi(self):
        raise AttributeError, "Can't delete attribute."

    efermi = property(_get_efermi, _set_efermi, _del_efermi, "Fermi energy.")

    def get_energygrid(self):
        """Return the array with the energies."""
        return self.dos[1, :, 0]

    def get_dos(self, atom, orbital):
        """Return an NDOSx1 array with dos for the chosen atom and orbital.
        
        If spin-unpolarized calculation, no phase factors:
        s = 1, p = 2, d = 3
        Spin-polarized, no phase factors:
        s-up = 1, s-down = 2, p-up = 3, p-down = 4, d-up = 5, d-down = 6
        If phase factors have been calculated, orbitals are
        s, py, pz, px, dxy, dyz, dz2, dxz, dx2
        double in the above fashion if spin polarized.
        
        """
        return self.dos[atom, :, orbital]


def set_labels(fig=None):
    """Utility function to set default parameters for DOS plots."""

    plt.xlabel("E-E$_\mathrm{f}$ (eV)")
    plt.figtext(0., 0.35, "LDOS (arb. units)", rotation='vertical')
    if fig is not None:
        # Looks good in publication plots
        fig.subplots_adjust(hspace=0.0, left=0.15, bottom=0.12)
    else:
        # This might be better for on-screen viewing
        plt.subplots_adjust(hspace=0.0)

