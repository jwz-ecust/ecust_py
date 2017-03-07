# -*- coding: utf-8 -*-
import numpy
import os
import re
import csv


data_path = "/Volumes/WD/data/NiP_data"


def get_final_energy(oszicar_path):
    '''
    给定 OSZICAR 文件的路径
    通过正则获取能量数据
    并返回最后一步的能量
    '''
    with open(oszicar_path) as fuck:
        return float(re.findall('E0= (.+?\+\d{2})', fuck.read())[-1])


# 获取吸附能
energy_of_CO = -14.7714764    # 这是一个平均值, 反正也无所谓, 都是一起减掉的
surface_path = data_path + "/surface/oszicar"
co_and_surface_path = data_path + "/surface_and_CO/oszicar"

csvfile = file('NiP_data.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['E_ads', 'Bond_dis', 'Angle', 'Matrix',
                 'Pauling', 'Coordinate_number'])

for num in range(1, 111):
    surface = surface_path + "/OSZICAR_{}".format(num)
    co_and_surface = co_and_surface_path + "/OSZICAR_{}".format(num)
    energy_of_surface = get_final_energy(surface)
    energy_of_CO_and_surface = get_final_energy(co_and_surface)
    energy_of_adsorption = energy_of_CO_and_surface - energy_of_surface - energy_of_CO
    writer.writerow([energy_of_adsorption])

csvfile.close()
