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
'''
work_path = "./machine-learning-data/NiP-ads/work"
for i in sftp.listdir(work_path):
    if i.startswith('USPEX'):
        print i


# 开始下载文件:
for i in range(1, 111):
    remote_outcar_path = work_path + "/" + \
        "USPEX_generation_{}".format(i) + "/CONTCAR"
    local_outcar_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/data/{}CONTCAR".format(
        i)
    remote_doscar_path = work_path + "/" + \
        "USPEX_generation_{}".format(i) + "/dos_cal/step2/DOSCAR"
    local_doscar_path = "/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/data/{}DOSCAR".format(
        i)
