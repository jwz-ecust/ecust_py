import os
import shutil

dir = "/Users/zhangjiawei/Pictures/captcha/split_pics"


files = os.listdir(dir)
for pic in files:
    p = os.path.join(dir, pic)
    size = os.path.getsize(p)
    if size < 500:
        os.remove(p)
