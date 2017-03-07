import paramiko
import os


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
IP = "219.220.210.138"
port = 2200
user = "jwzhang"
key = "/Users/zhangjiawei/.ssh/id_dsa_138_jwzhang.jwzhang"
ssh.connect(IP, port, user, key_filename=key)
# stdin, stdout, stderr = ssh.exec_command('qstat -a')


sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
work_path = "./machine-learning-data/NiP-ads/work"
ml = sftp.listdir(work_path)
a = ml[0]
down_path = work_path + '/' + a + '/' + 'OUTCAR'
sftp.get(down_path, '/Users/zhangjiawei/Code/zjw/paramiko_ssh/outcar')
