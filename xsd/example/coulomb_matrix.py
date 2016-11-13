import xml.etree.cElementTree as ET
import os
import numpy as np

path = os.getcwd()
path = os.path.join(path, 'example/1.xsd')

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
