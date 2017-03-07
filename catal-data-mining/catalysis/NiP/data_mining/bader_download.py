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

    remote_bader_path = work_path + "/" + \
        "USPEX_generation_{}".format(i) + "/dos_cal/step1/ACF.dat"
    local_bader_path = "/Volumes/WD/data/NiP_data/surface/bader/ACF_{}.dat".format(
        i)

    sftp.get(remote_bader_path, local_bader_path)


print "finishing download!"
