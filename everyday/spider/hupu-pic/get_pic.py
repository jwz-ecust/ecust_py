# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import StringIO
from PIL import Image
import urllib
import urllib2


def save(url, p_path):
    # r = requests.get(url)
    picture = p_path + '/' + url.split('/')[-1].strip()
    # i = Image.open(StringIO.StringIO(r.content))
    # i.save(picture)
    u = urllib.urlopen(url)
    data = u.read()
    with open(picture, 'wb') as fff:
        fff.write(data)

    # with open(picture, 'wb') as ff:
    #     for chunk in r.iter_content(chunk_size=1024):
    #         ff.write(chunk)


p_path = '/Users/zhangjiawei/Pictures/2017/hupu_photo'

with open('./urls.txt', 'r') as fuck:
    urls = fuck.readlines()
    for url in urls:
        url = 'http:' + url
        print url
        save(url, p_path)
