# -*- coding: utf-8 -*-
"""
这个代码只用来识别如下URL的验证码，仅通过二值化处理即可进行文本识别，这里需要安装PIL库，需要安装tesseract并加入环境变量。
"""
from PIL import Image  # 需要加载PIL库
import os
# import urllib
import StringIO
import pytesseract  # 这是我自己写的
# url = 'http://202.119.81.113:8080/verifycode.servlet'  # 验证码URL
# r = urllib.urlopen(url)
# f = open('VCode.jpg', 'wb')    #这里是将验证码图片写入到本地文件
# f.write(r.read())
# f.close()
# imgBuf = StringIO.StringIO(r.read())  # 采用StringIO直接将验证码文件写到内存，省去写入硬盘
img = Image.open(imgBuf)  # PIL库加载图片
print img.format, img.size, img.mode  # 打印图片信息，可以删去
img = img.convert('RGBA')  # 转换为RGBA
pix = img.load()  # 读取为像素
for x in range(img.size[0]):  # 处理上下黑边框
    pix[x, 0] = pix[x, img.size[1] - 1] = (255, 255, 255, 255)
for y in range(img.size[1]):  # 处理左右黑边框
    pix[0, y] = pix[img.size[0] - 1, y] = (255, 255, 255, 255)
for y in range(img.size[1]):  # 二值化处理，这个阈值为R=95，G=95，B=95
    for x in range(img.size[0]):
        if pix[x, y][0] < 95 or pix[x, y][1] < 95 or pix[x, y][2] < 95:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 255)
img.save("temp.jpg")  # 由于tesseract限制，这里必须存到本地文件
text = pytesseract.image_to_string("temp.jpg")
os.remove('temp.jpg')
if len(text) == 4:  # 正确的验证码只含有4个字符
    text.replace('l', '1')  # 消除‘1’识别为‘l’的错误
    print text  # 这里即为最终识别的验证码
else:
    print '0'  # 如果识别错误
