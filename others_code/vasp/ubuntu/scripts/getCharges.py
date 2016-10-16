#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
getCharges
----------

NAME
        getCharges - compute atomic charges

SYNTAX
        getCharges [OPTIONS]

DESCRIPTION
        Compute atomic charges from a Bader caclculations done with the bader program of
        the University of Texas at Austin :

        http://theory.cm.utexas.edu/bader/

        Requirements :
            * a ACF.dat file (bader output)
            * a vasprun.xml file or a POSCAR/CONTCAR file of the structure.

        options :
            -h, --help
                print this help and exit
"""

import sys
import os
from math import sqrt, fabs

import vasptools
import crystal

__author__ = "Germain Vallverdu <germain.vallverdu@univ-pau.fr>"
__licence__ = "GPL"

def getCharges():
    """ compute charges """

    #
    # print documentation
    #
    args = sys.argv
    if "-h" in args or "--help" in args:
        print(__doc__)
        exit(0)

    #
    # read atom names
    #
    if os.path.exists("vasprun.xml"):
        run = vasptools.VaspRun("vasprun.xml", verbose = False)
        atomNames = list()
        for atom in run.atoms:
            atomNames.append(atom.name)

    elif os.path.exists("POSCAR"):
        struct = crystal.Crystal.fromPOSCAR("POSCAR", verbose = False)
        if struct.atomNames[0] == "X1":
            print("Please, add atom names to the POSCAR file")
            exit(1)
        atomNames = struct.atomNames

    elif os.path.exists("CONTCAR"):
        struct = crystal.Crystal.fromPOSCAR("CONTCAR", verbose = False)
        if struct.atomNames[0] == "X1":
            print("Please, add atom names to the CONTCAR file")
            exit(1)
        atomNames = struct.atomNames

    nat = len(atomNames)

    #
    # System composition and valence electron
    #
    composition = dict()
    valence = dict()
    print("Number of valence electrons ?")
    for name in atomNames:
        if name not in composition.keys():
            composition[name] = 1
            try:
                valence[name] = int(raw_input(name.ljust(5) + " = "))
            except ValueError:
                print("An integer is required")
                exit(1)
        else:
            composition[name] += 1

    #
    # read population from ACF.dat file
    #
    acf = open("ACF.dat", "r").readlines()[2:]

    iat = 0
    population = list()
    for line in acf:
        if "------------" in line:
            break
        population.append(float(line.split()[4]))
        iat += 1

    if iat != nat:
        print("Error, number of atom in ACF.dat not consistent")

    #
    # output
    #
    print("\n   i  name   Z      pop       charge")
    print("------------------------------------")
    for iat in range(nat):
        charge = valence[atomNames[iat]] - population[iat]
        print("%4d %4s %4d %10.4f %10.4f" % (iat + 1, atomNames[iat], valence[atomNames[iat]], population[iat], charge))
    print("------------------------------------\n")

    #
    # average charges
    #
    avePop = dict()
    av2Charge = dict()
    for name in composition.keys():
        avePop[name] = 0.
        av2Charge[name] = 0.

    line = ""
    for name in composition.keys():
        line += "%s_%d " % (name, composition[name])
    print("Composition : {0}\n".format(line))

    for iat in range(nat):
        name = atomNames[iat]
        avePop[name] += population[iat]
        av2Charge[name] += (valence[name] - population[iat])**2

    print("Averages :")
    print(" name   Z          charge")
    print("------------------------------------")
    for name in composition.keys():
        avePop[name] /= float(composition[name])
        charge  = valence[name] - avePop[name]

        av2Charge[name] /= float(composition[name])
        if fabs(av2Charge[name] - charge**2) < 1e-5:
            av2Charge[name] = 0.
        else:
            av2Charge[name] = sqrt(av2Charge[name] - charge**2)

        print("%4s %4d %10.4f +/- %7.4f" % (name, valence[name], charge, av2Charge[name]))
    print("------------------------------------\n")

if __name__ == "__main__":
    getCharges()
