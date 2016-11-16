# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


with open('./urls.txt', 'r') as f:
    urls = f.readlines()
    number = 0
    path = '/Users/zhangjiawei/Pictures/hupu_photo'
    for pic in urls:
        r = requests.get(pic, stream=True, timeout=10)
        pic_path = path + '/' + str(number) + pic.split('/')[-1].strip()
        with open(pic_path, 'wb') as ff:

        number = number + 1


# number = 0
# pic_path = '/Users/zhangjiawei/Pictures/hupu_photo'
# for pic_url in sub_pic_url_list:
#     r = requests.get(pic_url, stream=True, timeout=10)
#     pic = pic_path + '/' + str(number) + '.jpg'
#     number = number + 1
#     with open(pic, 'w') as f:
