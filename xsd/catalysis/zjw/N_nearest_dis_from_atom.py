# -*- coding:utf-8 -*-
import xml.etree.cElementTree as ET
import os
import numpy as np

'''
用来获取距离最近的N个原子(N比如说10...)
返回一个list 包含了到所有其他原子的距离
'''
path = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/NiP.xsd'


root = ET.ElementTree(file=path)

id_map = root.findall('.//IdentityMapping')
print id_map

atom_list = []
coordiante_list = []
for element in root.iter():
    # print "Tag:%s\nAttrib:%s\nText:%s" % (element.tag, element.attrib,
    #                                       element.text)
    if element.attrib.has_key('XYZ'):
        atom = element.attrib['Components']
        coordiante = element.attrib['XYZ'].split(',')
        atom_list.append(atom)
        coordiante_list.append(coordiante)


atom_matric = np.array(coordiante_list, dtype=np.float)

t_atom = atom_matric[0]
dis_list = []
for i in range(1, len(atom_matric)):
    dis = np.sqrt(sum((atom_matric[i] - t_atom)**2))
    dis_list.append(dis)

print dis_list
