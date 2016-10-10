# -*- coding: utf-8 -*-

from PIL import Image
import glob
import os

def reSize(dirPath,sizeX= 100, sizeY = 100):
    for file in glob.glob(dirPath +'*.jpg'):
        print file
        ori = Image.open(file)
        modi = ori.resize((sizeX,sizeY))
        modi.save(os.path.splitext(file)[0]+'_modified'+'.jpg')

reSize('pics/',300,200)