# -*- coding: utf-8 -*-
import paramiko
import sys
import time

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

name = time.strftime("%Y%m%d_%H%M", time.localtime())
