# -*- coding: utf-8 -*-
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


class login_info(object):

    def __init__(self, ip, port, user, password=None, key=None):
        self.ip = ip
        self.port = port
        self.user = user
        if password == None:
            self.key = key
        else:
            self.password = password


zjw = login_info('219.220.210.138', 2200, 'jwzhang',
                 key='/Users/zhangjiawei/.ssh/id_dsa_138_jwzhang.jwzhang')

ssh.connect(zjw.ip, zjw.port, zjw.user, key_filename=zjw.key)

sftp = ssh.open_sftp()

'''
需要下载的文件:
    1. USPEX_generation_number/CONTCAR
    2. USPEX_generation_number/dos_cal/step2/DOSCAR
    3. Energy of slab
    4. Energy of CO+slab
How to download:
sftp.get(remote_path, local_path)
'''


# 开始下载文件:
work_path = "/home/users/jwzhang/machine-learning-data/NiP-ads/work"
print "startig download......."

for i in range(1, 111):
    print "{:.6f}%: ".format(i / 1.110), ">" * (i * 100 / 111)
    # remote_contcar_path = work_path + "/" + \
    #     "USPEX_generation_{}".format(i) + "/CONTCAR"
    # local_contcar_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/data/slab/CONTCAR_slab_{}".format(
    #     i)
    # remote_doscar_path = work_path + "/" + \
    #     "USPEX_generation_{}".format(i) + "/dos_cal/step2/DOSCAR"
    # local_doscar_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/data/dos/DOSCAR_{}".format(
    #     i)
    # remote_contcar_co_path = work_path + "/" + \
    #     "USPEX_generation_{}".format(i) + "/CO/CONTCAR"
    # local_contcar_co_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/data/CO/CONTCAR_CO_{}".format(
    #     i)
    # remote_outcar_path = work_path + "/" + \
    #     "USPEX_generation_{}".format(i) + "/OUTCAR"
    # local_outcar_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/data/outcar/OUTCAR_{}".format(
    #     i)
    # remote_oszicar_path = work_path + "/" + \
    #     "USPEX_generation_{}".format(i) + "/OSZICAR"
    # local_oszicar_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/data/oszicar/OSZICAR_{}".format(
    #     i)

    remote_oszicar_co_path = work_path + "/" + \
        "USPEX_generation_{}".format(i) + "/CO/OSZICAR"
    local_oszicar_co_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/data/surface_and_CO/oszicar/OSZICAR_{}".format(
        i)

    remote_outcar_co_path = work_path + "/" + \
        "USPEX_generation_{}".format(i) + "/CO/OUTCAR"
    local_outcar_co_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/data/surface_and_CO/outcar/OUTCAR_{}".format(
        i)

    sftp.get(remote_outcar_co_path, local_outcar_co_path)
    sftp.get(remote_oszicar_co_path, local_oszicar_co_path)


print "finishing download!"
