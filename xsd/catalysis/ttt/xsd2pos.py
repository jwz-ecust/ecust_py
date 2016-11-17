# -*- coding: utf-8 -*-
# author: jwz-ecust
# mail: jwz_ecust@mail.ecust.edu.cn

import xml.etree.cElementTree as ET
import os
import numpy as np


def xsd2pos(file_path, pos_path):
    '''
    read data from xsd file to generate POSCAR
    '''
    root = ET.ElementTree(file=file_path)
    # get the spacegroup infor
    direction = ['A', 'B', 'C']
    # Xpath 寻找任意属性 .//attribute_name
    spacegroup = root.find(".//SpaceGroup")
    lattice_info = np.zeros((3, 3))
    for i in range(3):
        key_name = '{}Vector'.format(direction[i])
        lattice_info[i] = spacegroup.get(key_name).split(',')

    '''
    atom_info:
        [[  6.05         0.           0.        ]
         [  0.           9.762        0.        ]
         [  0.           0.          20.50356631]]
    '''

    atom_list = []
    coordiantes_list = []

    for element in root.iter():

        if 'XYZ' in element.keys() and 'Components' in element.keys():
            atom_name = element.get('Components')
            coordiante = element.get('XYZ').split(',')
            atom_list.append(atom_name)
            coordiantes_list.append(coordiante)

    '''
    Coordinates:
    ['0.460897436328624', '0.378911191842066', '0.009711118307051']
    ['0.460897436328624', '0.878911191842066', '0.009711118307051']
    ['0.051962577235302', '0.128862121650187', '0.009850222396201']
    ['0.051962577235302', '0.628862121650187', '0.009850222396201']
    ['0.955282613315399', '0.458394731739651', '0.092462817901284']
    ['0.955282613315399', '0.958394731739651', '0.092462817901284']
    ['0.557727413243300', '0.208608617045294', '0.092542836360121']
    ['0.557727413243300', '0.708608617045294', '0.092542836360121']
    ['0.438690232325942', '0.390700001290171', '0.172391673920641']
    ['0.438690232325942', '0.890700001290171', '0.172391673920641']
    ['0.074955761365656', '0.140753942691418', '0.172428734590077']
    ['0.074955761365656', '0.640753942691419', '0.172428734590077']
    ['0.949876677677532', '0.371776500984694', '0.261388887033405']
    ['0.949876677677532', '0.871776500984694', '0.261388887033405']
    ['0.564061347447952', '0.121611378143702', '0.261393692675875']
    ['0.564061347447952', '0.621611378143702', '0.261393692675875']
    ['0.448907163837217', '0.446967886922733', '0.339330806312637']
    ['0.448907163837217', '0.946967886922733', '0.339330806312637']
    ['0.065194115953033', '0.196842872915870', '0.339352262288949']
    ['0.065194115953033', '0.696842872915869', '0.339352262288949']
    ['0.964128435024480', '0.453123547690723', '0.428475863584505']
    ['0.964128435024480', '0.953123547690723', '0.428475863584505']
    ['0.550361721459678', '0.202997629682373', '0.428486850354934']
    ['0.550361721459678', '0.702997629682373', '0.428486850354934']
    ['0.465842676653832', '0.371825134112270', '0.509338735304974']
    ['0.465842676653832', '0.871825134112270', '0.509338735304974']
    ['0.048922828246857', '0.121741771124466', '0.509366748257662']
    ['0.048922828246857', '0.621741771124466', '0.509366748257662']
    ['0.702350500911176', '0.047387250433748', '0.029609496621496']
    ['0.702350500911176', '0.547387250433748', '0.029609496621496']
    ['0.810643305065648', '0.297294181658323', '0.029600583265148']
    ['0.810643305065648', '0.797294181658323', '0.029600583265148']
    ['0.311059621554058', '0.037184374748357', '0.089007194627093']
    ['0.311059621554058', '0.537184374748356', '0.089007194627093']
    ['0.202083825392728', '0.287144869435161', '0.088907854279032']
    ['0.202083825392728', '0.787144869435161', '0.088907854279032']
    ['0.806417952028920', '0.301317385204539', '0.165479994702201']
    ['0.806417952028920', '0.801317385204539', '0.165479994702201']
    ['0.707380533528185', '0.051178708973613', '0.165573639096929']
    ['0.707380533528185', '0.551178708973613', '0.165573639096929']
    ['0.309779193624166', '0.291037847114931', '0.264144343056449']
    ['0.309779193624166', '0.791037847114931', '0.264144343056449']
    ['0.204230605422742', '0.041068693507885', '0.264187939176388']
    ['0.204230605422742', '0.541068693507885', '0.264187939176388']
    ['0.815846843932813', '0.026573924299544', '0.332240611123416']
    ['0.815846843932813', '0.526573924299543', '0.332240611123416']
    ['0.698187812472172', '0.276569888168488', '0.332241838236385']
    ['0.698187812472172', '0.776569888168488', '0.332241838236385']
    ['0.316862408457499', '0.027325298390892', '0.437804870896472']
    ['0.316862408457499', '0.527325298390893', '0.437804870896472']
    ['0.197951525387305', '0.277230803331790', '0.437739062149150']
    ['0.197951525387305', '0.777230803331790', '0.437739062149150']
    ['0.808477435330847', '0.292518577120333', '0.490018195527824']
    ['0.808477435330847', '0.792518577120333', '0.490018195527824']
    ['0.706286135037044', '0.042475963798737', '0.489979160970230']
    ['0.706286135037044', '0.542475963798737', '0.489979160970230']
    '''

    '''
    atom list:
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'Ni', 'Ni',
            'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni']
    '''
    # pos_path = './POSCAR'

    # 生成有序的列表   类似这样['P','Ni'],[28, 28]
    atom = []
    for i in atom_list:
        if i not in atom:
            atom.append(i)
    atom_number = [str(atom_list.count(i)) for i in atom]
    # print atom_number, atom

    with open(pos_path, 'w') as fuk:
        fuk.write('zjw uspex generated structure opt\n')
        fuk.write('1.0000\n')
        # 写入晶胞参数矩阵
        for i in range(3):
            string = ' ' * 5 + '   '.join([str(i).center(12)
                                           for i in lattice_info[i]]) + '\n'
            fuk.write(string)
        # 写入原子种类
        fuk.write(' ' * 4 + '    '.join([_.center(2) for _ in atom]) + '\n')
        # 写入原子数
        fuk.write(' ' * 4 + '    '.join([_.center(2)
                                         for _ in atom_number]) + '\n')

        fuk.write('Selective dynamics\n')
        fuk.write('Direct\n')
        # 写入对应坐标
        cor_length = len(coordiantes_list)
        for i in range(cor_length):
            string = '  ' + \
                '  '.join([_.ljust(18)
                           for _ in coordiantes_list[i]]) + '   T' * 3 + '\n'
            fuk.write(string)

origin_path = os.getcwd()
# origin_path = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/ttt'
xsd_path = os.path.join(origin_path, 'xsds')
work_path = os.path.join(origin_path, 'work')

xsds = os.listdir(xsd_path)
for i in xsds:
    print i
    xsd = os.path.join(xsd_path, i)
    name = i.split('.')[0]
    dis_path = os.path.join(work_path, name)
    os.mkdir(os.path.join(dis_path))
    pos_path = os.path.join(dis_path, 'POSCAR')
    xsd2pos(xsd, pos_path)
