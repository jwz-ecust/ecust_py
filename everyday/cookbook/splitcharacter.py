from PIL import Image
import numpy as np


pic = "/Users/zhangjiawei/Pictures/captcha/binarizing/1002.png"
characters = "dights"


image = Image.open(pic)
img = np.array(image)



linesum = img.sum(axis=0)
indexs = []
for i in range(img.shape[-1]-1):
    if linesum[i] >= 44880 and linesum[i+1] < 44880:
        indexs.append(i)

reverse = 0

for j in range(img.shape[1]):
    flag = all(linesum[j:] == 45900)
    if flag:
        reverse = j
        break

indexs.append(reverse)
for i in range(len(indexs)-1):
    subchar = img[:, indexs[i]:indexs[i+1]]
    subimage = Image.fromarray(subchar)
    subimage.save("./{}.jpg".format(str(i)))


'''
[75, 146, 235, 314, 367]           45900
[74, 146, 171, 236, 314, 368]      45645
[74, 146, 171, 236, 314, 368]      45390
[74, 146, 171, 236, 314, 368]      45135
[76, 146, 171, 236, 314, 368]      44880
[76, 146, 171, 237, 315, 370]      44625
'''
