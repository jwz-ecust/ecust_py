# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import urllib2


def get_soup(url):
    _html = requests.get(url)
    _content = _html.text.encode('utf-8')
    return BeautifulSoup(_content, 'html.parser')


link_list = []
o_url = 'http://photo.hupu.com'
for i in range(1, 7):
    num = i
    url = 'http://photo.hupu.com/tag/gif?p={}&o=1'.format(num)
    # r = requests.get(url)
    # content = r.text.encode('utf-8')
    # soup = BeautifulSoup(content, 'html.parser')
    soup = get_soup(url)
    for lin in soup.find_all('a', class_='ku'):
        link_list.append(o_url + lin.get('href'))
        # 获取所有的git 子网页 存入列表 link_list
s = 0
# for i in link_list:
#     print i
#     soup = get_soup(i)
#     #  获取子网页图片数
#     number = soup.find('span', class_='nomp').contents[3]
#     number = number.encode(
#         'utf-8').split('\xa0')[1].split('\xc2')[0].strip(')')
#     print number


url_link = 'http://photo.hupu.com/p8585.html'
soup = get_soup(url)
a = soup.find('span', class_='nomp')
print a
