#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
postDOS
-------

NAME
        postDOS - extract DOS from vasprun.xml

SYNTAX
        postDOS [OPTIONS]


DESCRIPTION
        Extract the total DOS and projected DOS from a VASP calculation. All DOS are summed on
        spin up and down. 

        output :
            sommeDOS.dat : contains the total DOS and the sum of all projected DOS. 
            DOS_XX.dat   : contains the contribution of atoms XX to the DOS. One file by atom type.

        options

        -h, --help
            print this help and exit

        -iat N
            output the contribution of atom N to the total DOS. N is in [1; Natom]
"""

__author__ = "Germain Vallverdu <germain.vallverdu@univ-pau.fr>"
__licence__ = "GPL"

import sys
import vasptools
import numpy as np

def postDOS():

    # ----------------------------------------------------------
    # defaults
    # ----------------------------------------------------------
    xml = "vasprun.xml"
    oneatom = False

    # ----------------------------------------------------------
    # arguments
    # ----------------------------------------------------------
    args = sys.argv
    if "-h" in args or "--help" in args:
        print(__doc__)
        exit(0)

    elif "-iat" in args:
        try:
            iat = int(args[args.index("-iat") + 1]) - 1
        except:
            print("Error : -iat must be followed by an integer")
            exit(1)
        if iat < 0:
            print("iat : {0}".format(iat + 1))
            print("Error : iat must be in [1; Natomes]")
            exit(1)
        oneatom = True

    # ----------------------------------------------------------
    # extract DOS
    # ----------------------------------------------------------
    calcul = vasptools.VaspRun(xml, verbose=False)
    calcul.lectureDOS()
    if not calcul.DOSPartiellesLues:
        print("Error when reading DOS in {0}".format(xml))
        exit(1)

    # ----------------------------------------------------------
    # DOS treatment
    # ----------------------------------------------------------
    if oneatom:
        if iat > calcul.Natomes - 1:
            print("iat : {0}".format(iat + 1))
            print("Error : iat must be in [1; Natomes]")
            exit(1)
        atomContribution(calcul, iat)
    else:
        globalTreatment(calcul)

def atomContribution(calcul, iat):
    """ extract the contribution of atom iat to the total DOS """

    # spin polarized ?
    ispin = calcul.allMotsClefs["ISPIN"]

    # energies
    energie = [e - calcul.eFermi for e in calcul.energiesDOS]

    # dos of atom iat
    atomDOS = np.array(calcul.dosPartielles[iat])
    
    # print DOS of atom iat  
    out  = "# Contribution of atom {0} {1} to the total DOS\n".format(calcul.atoms[iat].name, iat + 1)
    out += "# 1 : E - Ef (eV) \n"
    if ispin == 2:
        out += "# 2 : DOS up \n"
        out += "# 3 : DOS down \n"
        out += "# 4 : AO s up \n"
        out += "# 5 : AO s down \n"
        out += "# 6 : AO p up\n"
        out += "# 7 : AO p down\n"
        out += "# 8 : AO d up\n"
        out += "# 9 : AO d down\n"
        for e, dosup, dosdown in zip(energie, atomDOS[0], atomDOS[1]):
            sdosup = dosup[0]
            pdosup = dosup[1] + dosup[2] + dosup[3]
            ddosup = dosup[4] + dosup[5] + dosup[6] + dosup[7] + dosup[8]
            sdosdown = dosdown[0]
            pdosdown = dosdown[1] + dosdown[2] + dosdown[3]
            ddosdown = dosdown[4] + dosdown[5] + dosdown[6] + dosdown[7] + dosdown[8]
            out += "%12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f\n" % \
                (e, dosup.sum(0), -dosdown.sum(0), sdosup, -sdosdown, \
                pdosup, -pdosdown, ddosup, -ddosdown)
    else:
        out += "# 2 : DOS \n"
        out += "# 3 : AO s \n"
        out += "# 4 : AO p \n"
        out += "# 5 : AO d \n"
        for e, dos in zip(energie, atomDOS[0]):
            sdos = dos[0]
            pdos = dos[1] + dos[2] + dos[3]
            ddos = dos[4] + dos[5] + dos[6] + dos[7] + dos[8]
            out += "%12.7f %12.7f %12.7f %12.7f %12.7f\n" % \
                (e, dos.sum(0), sdos, pdos, ddos)

    open("DOS_{0}{1}.dat".format(calcul.atoms[iat].name, iat + 1), "w").write(out)

def globalTreatment(calcul):
    """ extract the contribution of each atom type to the total DOS """

    # spin polarized ?
    ispin = calcul.allMotsClefs["ISPIN"]

    # energies
    energie = [e - calcul.eFermi for e in calcul.energiesDOS]

    #
    # total DOS
    #
    dosTotale = np.array(calcul.dosTotale)

    #
    # DOS partielles
    #
    dosPartielles = np.array(calcul.dosPartielles)

    # composition du systeme
    composition = dict()
    for atom in calcul.atoms:
        if atom.name not in composition.keys():
            composition[atom.name] = 1
        else:
            composition[atom.name] += 1

    for element in composition.keys():
        print("Nbre de %2s = %d" % (element, composition[element]))

    # number of different atoms
    nType = len(composition)

    # DOSparAtom
    nspin, npts, nOA = dosPartielles[0,:,:,:].shape
    DOSparAtom = np.zeros((nType, nspin, npts, nOA))

    # sum of projected DOS
    sommeDOSpartielles = np.zeros((npts,nOA))

    for iat in range(len(calcul.atoms)):
        itype = calcul.atoms[iat].atomType - 1
        DOSparAtom[itype] += dosPartielles[iat,:,:,:]
        sommeDOSpartielles += dosPartielles[iat,0,:,:]
        if ispin == 2:
            sommeDOSpartielles += dosPartielles[iat,1,:,:]

    # print sum of projected DOS
    out = "# Total DOS and sum of all projected DOS\n"
    if ispin == 2:
        out += "#                     Total DOS\n"
        out += "#   E (eV)       DOS up       DOS down     sum\n"
        for e, dosup, dosdown, sumDOS in zip(energie, dosTotale[0,:,0], dosTotale[1,:,0], sommeDOSpartielles.sum(1)):
            out += "%12.7f %12.7f %12.7f %12.7f\n" % (e, dosup, -dosdown, sumDOS)
    else:
        out += "#   E (eV)       DOS          sum\n"
        for e, dos, sumDOS in zip(energie, dosTotale[0,:,0], sommeDOSpartielles.sum(1)):
            out += "%12.7f %12.7f %12.7f\n" % (e, dos, sumDOS)
    open("sommeDOS.dat", "w").write(out)

    # print one file per atom
    for itype in range(nType):
        for atom in calcul.atoms:
            if itype == atom.atomType - 1:
                name = atom.name.strip()
                break
        out  = "# Contribution of {0} atoms to the total DOS\n".format(name)
        out += "# 1 : E - Ef (eV) \n"
        if ispin == 2:
            out += "# 2 : DOS up \n"
            out += "# 3 : DOS down \n"
            out += "# 4 : AO s up \n"
            out += "# 5 : AO s down \n"
            out += "# 6 : AO p up\n"
            out += "# 7 : AO p down\n"
            out += "# 8 : AO d up\n"
            out += "# 9 : AO d down\n"
            for ene, dosup, dosdown in zip(energie, DOSparAtom[itype,0,:,:], DOSparAtom[itype,1,:,:]):
                pup = dosup[1] + dosup[2] + dosup[3]
                dup = dosup[4] + dosup[5] + dosup[6] + dosup[7] + dosup[8]
                pdown = dosdown[1] + dosdown[2] + dosdown[3]
                ddown = dosdown[4] + dosdown[5] + dosdown[6] + dosdown[7] + dosdown[8]
                out += "%12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f %12.7f\n" % \
                    (ene, dosup.sum(), -dosdown.sum(), dosup[0], -dosdown[0], \
                    pup, -pdown, dup, -ddown)
        else:
            out += "# 2 : DOS \n"
            out += "# 3 : AO s \n"
            out += "# 4 : AO p \n"
            out += "# 5 : AO d \n"
            for ene, dos in zip(energie, DOSparAtom[itype,0,:,:]):
                pdos = dos[1] + dos[2] + dos[3]
                ddos = dos[4] + dos[5] + dos[6] + dos[7] + dos[8]
                out += "%12.7f %12.7f %12.7f % 12.7f %12.7f\n" % (ene, dos.sum(), dos[0], pdos, ddos)
        open("DOS_{0}.dat".format(name), "w").write(out)

if __name__ == "__main__":
    postDOS()

