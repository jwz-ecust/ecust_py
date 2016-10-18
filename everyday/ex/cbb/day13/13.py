#!/usr/bin/env python
# coding:utf-8

'''
如果代码的路径为 path/Newtouch.py
vim ~/.bashrc
添加 alias addth = 'python path/Newtouch.py' 一行
使其生效 source ~/.bashrc
测试一下
    addth foo.py
对应其他语言在代码中 herder_msg字典中添加相应头部信息即可
    例如C语言 'c':'#include <studio.h>\n'
'''

import os
import argparse
print 'current dir ====> {0}\n{1}'.format(os.getcwd(), '*' * 40)
parser = argparse.ArgumentParser(description='A script for adding script header message)
parser.add_argument('newfile')

args = parser.parse_args()

header_msg = {
    'py': '#!/usr/bin/env python\n# coding:utf-8\n# author: zjw\n',
    'c': '#include <stdio.h>\n'
}

if os.path.exists(os.getcwd() + '/' + args.newfile):
    print '\tfile already exists....'
else:
    if len(args.newfile.split('.')) == 2:
        newfile_type = args.newfile.split('.')[-1]
        if newfile_type in header_msg:
            with open(args.newfile, 'w') as f:
                print '\tadding header msg...'
                f.write(header_msg['py'])
                msg = 'created %s' % args.newfile
                print msg.center(40, '*')
        else:
            temp = open(args.newfile, 'w')
            temp.close()
            print '\tcreated ', args.newfile
    else:
        temp = open(args.newfile, 'w')
        temp.close()
        print '\tcreated ', args.newfile
