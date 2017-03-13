# -*- coding: utf-8 -*-

import Image
import os
import sys


# python中文字符集函数方法
def encodeChinese(msg):
    type = sys.getdefaultencoding()
    return msg.decode('utf-8').encode(type)

# 图片类型检测方法


def check_imgMode(filedir):
    try:
        img = Image.open(filedir)
        return img.mode
    except:
        errInfo = encodeChinese('这不是图片') + str(filedir) + '\n'
        print errInfo
        return errInfo


# python检测文件后缀，返回文件后缀方法
def check_fileMode(filedir):
    ff = os.path.splitext(filedir)[1]
    return ff

# 打开一个文件图片的方法


def open_imgFile(filedir):
    im = Image.open(filedir)
    im.load()
    return im


# python输入被检测文件夹路径方法
def input_rootdir():
    print encodeChinese('请输入要检测的文件夹路径：')
    rootdir = raw_input()
    print rootdir
    return rootdir


# python输入错误日志路径方法
def input_logdir():
    print encodeChinese('请输入错误日志路径：')
    logdir = raw_input()
    print logdir
    return logdir


# 输入处理完成图片保存路径
def input_targetdir():
    print encodeChinese('请输入处理完成后文件保存路径：')
    targetdir = raw_input()
    return targetdir


# 检测文件大小
def check_fileSize(filedir):
    try:
        with open(filedir, 'rb') as f:
            f.seek(0, 2)
            fSize = f.tell()
            print 'fSize:' + str(type(fSize))
            return f.tell()
    except:
        print encodeChinese('获取文件大小时发生错误')


# 检测图片类型，大小，分辨率
def check_texture(rootdir, errLodDir):
    with open(errLodDir, 'w') as effFile:
        for parent, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                fName = filename
                filename = rootdir + os.sep + filename
                if check_fileMode(filename) in ['.jpg', '.png']:
                    fSize = check_fileSize(filename)
                    if (fSize / 1024 > 1024):
                        filename = parent + os.sep + fName
                        print rootdir
                        effFile.write(filename + '\n')
                        err_sizeFile = encodeChinese('文件大小超过1024')
                        effFile.write(
                            err_sizeFile +
                            ':' +
                            str(check_fileSize(filename) / 1024) +
                            '\n')
                    elif (fSize / 1024 <= 1024):
                        img = open_imgFile(filename)
                        imgSize = img.size
                        if (imgSize[0] % 64 != 0 or imgSize[1] % 64 != 0):
                            print parent
                            print filename
                            print img.size
                            errSize = img.size
                            err_bigFile = encodeChinese('文件分辨率错误')
                            effFile.write(err_bigFile)
                            effFile.write(str(errSize) + '\n')
                            effFile.write('\n')
                else:
                    outPath = parent + os.sep + fName
                    effFile.write(outPath + '\n')
                    err_file = encodeChinese('文件格式不对')
                    effFile.write(err_file)
                    effFile.write('\n')
                    print fName
