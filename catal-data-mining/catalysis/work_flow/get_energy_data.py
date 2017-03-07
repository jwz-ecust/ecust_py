import os
import re
import subprocess


class job_info(object):

    def __init__(self, site_number, d_band_center, Eads, colomb_matrix, angles, distances, electronegativity, next_number=10):
        self.site_number = site_number
        self.d_band_center = d_band_center
        self.Eads = Eads
        self.colomb_matrix = colomb_matrix
        self.angles = angles
        self.distances = distances
        self.electronegativity = electronegativity
        self.next_number = next_number


def get_force(outcar):
    output = subprocess.check_output(['grep', 'FORCES:', outcar])
    return float(output.strip().split('\n')[-1].split(" " * 4)[1])


def get_energy(oszicar):
    '''
     239 F= -.17406981E+03 E0= -.17406920E+03  d E =-.633488E-03  mag=     0.0000
     取E0 后面那个能量
     ===> 需要输入 OSZICAR 文件路径
    '''
    output = subprocess.check_output(
        ["grep", "F", oszicar]).strip().split('\n')
    return float(output[-1].strip(' ')[4])


work_dir = "/home/users/jwzhang/machine-learning-data/NiP-ads/work"

job_dirs = os.listdir(work_dir)
job_dirs = [_ for _ in job_dirs if _.startswith('USPEX')]

for subdir in job_dirs:
    full_path = os.path.join(work_dir, subdir)
    outcar = os.path.join(full_path, 'OUTCAR')
    co = os.path.join(full_path, 'CO')
    co_outcar = os.path.join(co, 'OUTCAR')
    if os.path.exists(outcar) and os.path.exists(co_outcar):
        force_slab = get_force(outcar)
        force_CO = get_force(co_outcar)
        if force_slab <= 0.05 and force_CO <= 0.05:
