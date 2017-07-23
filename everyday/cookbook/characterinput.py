import os
from PIL import Image

captcha = "/Users/zhangjiawei/Pictures/captcha/split_pics"
toml = "/Users/zhangjiawei/Pictures/captcha/ml"

pics = os.listdir(captcha)

for i in pics:
    p = os.path.join(captcha, i)
    print(p + "\n")
    img = Image.open(p)
    img.show()
    a = input("character: ")
    if a.isalpha():
        to = os.path.join(toml, a) + "/" + i
        os.rename(p, to)
    else:
        os.remove(p)
    img.close()
