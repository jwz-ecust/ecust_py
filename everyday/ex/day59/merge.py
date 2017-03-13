import glob
import os

def main():
    directory = []
    for dirs in os.walk("../"):
        directory.append(dirs)
    folders = directory[0][1]
    for ff in folders:
        if ff != ".git":
            allFiles = glob.glob(ff+"/*.py")
            for i in allFiles:
                print i



main()