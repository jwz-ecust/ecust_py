# -*- coding: utf-8 -*-
import shlex
import sys
import subprocess


'''
shlex模块实现了一个类来解析简单的类shell语法，可以用来编写领域特定的语言，或者解析加引号的字符串。
处理输入文本时有一个常见的问题，往往要把一个加引号的单词序列标识为一个实体。
根据引号划分文本可能与预想的并不一样，特别是嵌套有多层引号时。


'''

if len(sys.argv) != 2:
    print "pls specify one filename on the command line"
    sys.exit(1)

filename = sys.argv[1]
body = file(filename,'rt').read()
print "original:" ,repr(body)
print

print "TOKENS:"
lexer = shlex.split(body)
for token in lexer:
    print repr(token)


#小技巧, 用subprocess.Popen()调用带参数的shell命令
subprocess.Popen(shlex.split('ls -al'))