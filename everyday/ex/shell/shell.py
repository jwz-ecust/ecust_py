#!/bin/env python
# -*- coding: utf-8 -*-

'''
Shell 的运行流程。

启动之后注册自定义的命令函数（即建立命令与相应函数的映射关系），输出命令提示符 $ ，等待用户输入命令；
用户输入命令之后按下回车，Shell 程序就要获取命令；
Shell 程序对命令格式进行解析；
解析之后，调用相关函数进行处理，如果当前命令的相关函数不存在则转交给系统处理，并将执行结果反馈给用户界面；
再次输出命令提示符 $ ，等待用户输入命令。

====================================================================================

设定变量 status 作为 while 循环的条件，当接收到 exit 命令的时候，
执行 exit 函数，修改 status 的值为 0 从而退出程序。
'''

import sys
import os
import getpass
import signal
import socket
import shlex
import subprocess
import platform
from func import *

build_in_cmds = {}


def tokenize(string):
    # 将string按shell的语法规则进行分割
    # 返回string的分割列表
    # 其实就是按空格符将命令与参数分开
    # 比如 'ls -l /home/shiyanlou' 划分之后
    # ['ls','-l','/home/shiyanlou']
    return shlex.split(string)


def preprocess(tokens):

    # 用于处理之后的token
    processed_token = []
    for token in tokens:
        if token.startswith('$'):
            # os.getenv ()用于获取环境变量的值,比如'HOME'
            # 环境不存在则返回空
            processed_token.append(os.getenv(token[1:]))
        else:
            processed_token.append(token)
    return processed_token


def handler_kill(signum, frame):
    raise OSError("killed!")


def excute(cmd_tokens):

    # 'a' 模式表示以添加的方式打开指定文件
    # 这个模式下文件对象的 write 操作不会覆盖文件原有的信息，而是添加到文件原有信息之后

    with open(HISTORY_PATH,'a') as history_file:
        history_file.write(' '.join(cmd_tokens)+os.linesep)
    if cmd_tokens:
        # 获取命令
        cmd_name = cmd_tokens[0]
        # 获取命令参数
        cmd_args = cmd_tokens[1:]

        # 如果当前命令在命令表中
        # 则传入参数，调用相应的函数进行执行
        if cmd_name in build_in_cmds:
            return build_in_cmds[cmd_name](cmd_args)

        # 监听Ctrl-C信号
        signal.signal(signal.SIGINT,handler_kill)

        # 如果当前系统不是 Windows
        # 则创建子进程
        if platform.system() != "Windows":
            # Unix平台
            # 调用进程执行命令
            p = subprocess.Popen(cmd_tokens)

            # 父进程从子进程读取数据,直到读取到EOF
            # 这里主要用来等待子进程终止运行
            p.communicate()
        else:
            # Windows平台
            command = ' '.join(cmd_tokens)
            # 执行 command
            os.system(command)
        # 返回状态
    return SHELL_STATUS_RUN


def display_cmd_prompt():

    # getpass.getuser 用于获取当前用户名
    user = getpass.getuser()
    # socket.gethostname() 返回当前运行python的程序的机器的主机名
    hostname = socket.gethostname()
    # 获取当前的工作路径
    cwd = os.getcwd()

    # 获取路径cwd的最低一级目录
    # 比如 cwd = '/home/shiyanlou'
    # 执行后 base_dir = 'shiyanlou'
    base_dir = os.path.basename(cwd)
    # 如果用户位于用户的根目录下,用"~"代替目录名
    home_dir = os.path.expanduser("~")
    if cwd == home_dir:
        base_dir = '~'

    # 输出命令提示符
    if platform.system() != "Windows":
        sys.stdout.write("[\033[1;33m%s\033[0;0m@%s \033[1;36m%s\033[0;0m]$" %(user, hostname,base_dir))
    else:
        sys.stdout.write("[%s@%s %s]$ " %(user,hostname,base_dir))
    sys.stdout.flush()



def ignore_signals():
    if platform.system() != "Windows":
        # 忽略Ctrl-Z 信号
        signal.signal(signal.SIGTSTP,signal.SIG_IGN)
    # 忽略 Ctrl-C信号
    signal.signal(signal.SIGINT,signal.SIG_IGN)



def shell_loop():
    status = SHELL_STATUS_RUN

    while status == SHELL_STATUS_RUN:
        # 打印命令提示符, 心如 `[<user>@<hostname> <base_dir>]$`
        display_cmd_prompt()

        # 忽略Ctrl-Z 或者 Ctrl-C 信号
        ignore_signals()

        try:
            # 读取命令
            cmd = sys.stdin.readline()

            # 解析命令
            # 讲命令进行拆分,返回一个列表
            cmd_tokens = tokenize(cmd)

            # 预处理函数
            # 将命令中的环境变量与真实值惊现替换
            # 比如讲 $HOME 这样的变量替换成真实值

            cmd_tokens = preprocess(cmd_tokens)

            # 执行命令,返回shell的状态
            status = excute(cmd_tokens)
        except:
            # sys.exc_info 函数返回一个包含三个值的元组(type,value,traceback)
            # 这三个值产生于最近一次呗处理的异常
            # 儿我们这里只需要获取中间的值
            _,err,_ = sys.exc_info()
            print err


def register_command(name, func):
    '''
    注册命令,使命令与相应的处理函数建立映射关系
    :param name: 命令名
    :param func: 函数名
    '''

    build_in_cmds[name] = func


def init():
    """
    注册所有命令
    """
    register_command("cd", cd)
    register_command("exit", exit)
    register_command("getenv", getenv)
    register_command("history", history)


def main():
    # 在执行 shell_loop函数进行循环监听之前,首先进行初始化
    # 建立命令与函数的映射关系表
    init()

    # 处理命令的组程序
    shell_loop()


if __name__ == '__main__':
    main()
