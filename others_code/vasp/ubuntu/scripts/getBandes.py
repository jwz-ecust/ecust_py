#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
getBandes
---------

NAME     
        getBandes - extract energy bands from vasprun.xml

SYNTAX
        getBandes [OPTIONS] ... [FILE]

DESCRIPTION
        Read energy bands on vasprun.xml files and either extract them into files or plot
        them directly. The last argument has to be the xml file, if absent './vasprun.xml'
        will be used.

        -h, --help
            print this help

        -t, --tofiles
            Print energy bands into file files.

        -d, --directions
            Take care about direction lines of the brillouin zone along the ones energy
            bands are computed. If you use this option, one file is created for each
            direction. This option is relevant only when you want to print projected DOS
            into files.

        -q, --quiet
            Low verbosity
"""

import os
import sys
import vasptools

__author__ = "Germain Vallverdu <germain.vallverdu@univ-pau.fr>"
__licence__ = "GPL"

def usage(code):
    """ usage """
    print(__doc__)
    exit(code)

def die(m):
    """ print m and exit with code 1 """
    print(m)
    exit(1)

def getBandes():
    """ extraction des bandes du fichier vasprun.xml """

    # ----------------------------------------------------------
    # options par defaut
    # ----------------------------------------------------------
    xml          = "vasprun.xml"
    parDirection = False
    toFile       = False
    verbose      = True

    # ----------------------------------------------------------
    # gestion des options
    # ----------------------------------------------------------
    narg = len(sys.argv)
    if narg > 1:
        for i in range(narg)[1:]:
            if sys.argv[i] == "-h" or sys.argv[i] == "-help":
                usage(0)

            elif sys.argv[i] == "-d" or sys.argv[i] == "--directions":
                parDirection = True

            elif sys.argv[i] == "-t" or sys.argv[i] == "--tofiles": 
                toFile = True

            elif sys.argv[i] == "-q" or sys.argv[i] == "--quiet":
                verbose = False

            else:
                if i == narg - 1:
                    xml = sys.argv[i]
                else:
                    print(sys.argv)
                    print("Error : bad arguments")
                    usage(1)

    if not toFile and parDirection:
        print("Warnings : option -d (--directions) unrelevant. Add -t (--toFiles) option\n \
        to print enerby bands into files for each direction line of the brillouin zone.")
        parDirection = False

    if not os.path.exists( xml ):
        die("Error : file {0} does not exist".format(xml))

    # ----------------------------------------------------------
    # extraction des bandes d'energies
    # ----------------------------------------------------------
    calcul = vasptools.VaspRun(xmlFile = xml, verbose=verbose )
    bandesLues = calcul.lectureBandes()
    if not bandesLues:
        die("Error when reading bands in {0}".format(xml))

    if toFile:
        # impression des bandes d'energies
        listeFichiers = vasptools.bands.bandsToFiles(calcul, parDirection)

        # liste des fichiers créés
        if verbose:
            print("\nFichier(s) créé(s) : " + str(len(listeFichiers)))
            for fichier in listeFichiers:
                print("\t" + fichier )

    else:
        vasptools.bands.showBandes(calcul)

if __name__ == "__main__":
    getBandes()
