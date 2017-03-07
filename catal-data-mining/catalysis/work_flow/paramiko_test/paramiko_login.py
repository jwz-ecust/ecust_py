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

# _, stdout, _ = ssh.exec_command('ls')
# print stdout.readlines()

#  设置SFTP:
#   1.新建一个SFTPClient对象，该对象复用之前的SSH连接
#   2.直接在之前的ssh上建立sftp链接
# sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
sftp = ssh.open_sftp()

# 下载文件   sftp.get(remote_path, local_path)
path = "./machine-learning-data/NiP-ads/work/USPEX_generation_1/print-out"
sftp.get(path, '/Users/zhangjiawei/Code/zjw/xsd/catalysis/paramiko_test/print-out')
