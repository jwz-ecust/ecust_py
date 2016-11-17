import numpy as np


def get_d_band_center(path):
    dos_data = np.loadtxt(path)
    length = dos_data.shape[0]
    sum_multi = 0
    sum = 0
    for i in range(length - 1):
        delta = dos_data[i + 1, 0] - dos_data[i, 0]
        sum_multi = sum_multi + delta * \
            dos_data[i + 1, -1] * dos_data[i + 1, 0]
        sum = sum + delta * dos_data[i + 1, -1]
    return sum_multi / sum


for num in range(29, 57):
    path = '/Users/zhangjiawei/Code/zjw/xsd/catalysis/dos/datta/DOS{}'.format(
        str(num))
    print get_d_band_center(path)
