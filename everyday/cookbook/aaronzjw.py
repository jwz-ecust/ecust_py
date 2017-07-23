from PIL import Image
import numpy as np
import os

def split_pic(
    pic="/Users/zhangjiawei/Pictures/captcha/binarizing/1002.png",
    base = "/Users/zhangjiawei/Pictures/captcha/split_pics",
    tolerance=4):
    image = Image.open(pic)
    img = np.array(image)
    linesum = img.sum(axis=0)
    indexs = []
    tolerance_sum_of_pix = (180-tolerance) * 255

    for i in range(img.shape[-1]-1):
        if linesum[i] >= tolerance_sum_of_pix and linesum[i+1] < tolerance_sum_of_pix:
            indexs.append(i)

    reverse = 0
    for j in range(img.shape[1]):
        flag = all(linesum[j:] == 180 * 255)
        if flag:
            reverse = j
            break
    indexs.append(reverse)

    f = pic.split("/")[-1].split(".")[0]
    ff = base + "/" + f
    if not os.path.exists(ff):
        print("start to spliting pic: {}".format(pic))
        os.mkdir(ff)
        for i in range(len(indexs)-1):
            subchar = img[:, indexs[i]:indexs[i+1]]
            subimage = Image.fromarray(subchar)
            subimage.save(ff + "/{}.jpg".format(str(i)))
    else:
        print("already finished spliting pic: {}".format(pic))


picspath="/Users/zhangjiawei/Pictures/captcha/binarizing"
pics = os.listdir(picspath)
for i in pics:
    pp = os.path.join(picspath, i)
    split_pic(pic=pp)
