# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_html_cont(url):
    _html = requests.get(url)
    _content = _html.text.encode('utf-8')
    return _content


url = 'http://photo.hupu.com'
content = get_html_cont(url)

soup = BeautifulSoup(content, 'html.parser')

url_list = []
html_hp = soup.find('div', class_='hp-wrap')
for i in html_hp.find_all('a', class_='ku'):
    short_url = i['href']
    if not short_url.startswith('/'):
        short_url = '/' + short_url
    full_url = url + short_url
    url_list.append(full_url)

sub_pic_url_list = []
for _url in url_list:
    # 获取图片总数
    temp_con = get_html_cont(_url)
    _soup = BeautifulSoup(temp_con, 'html.parser')
    num = _soup.find('span', class_='nomp').contents[3]
    num = num.encode('utf-8').split('\xa0')[1].split('\xc2')[0].strip(')')
    num = int(num)
    for n in range(1, num + 1):
        t = _url.split('.')
        t[-2] = t[-2] + '-' + str(n)
        new_url = '.'.join(t)
        sub_pic_url_list.append(new_url)
        # 将获取的链接加入新的列表

# 获取图片的下载== ==保存链接
with open('./urls.txt', 'w') as f:
    for _url in sub_pic_url_list:
        _temp = get_html_cont(_url)
        ns = BeautifulSoup(_temp, 'html.parser')
        # f.write(_url + '\n')
        print ns
        s_url = ns.find(id='bigpicpic').get('src')
        f.write(s_url + '\n')


# number = 0
# pic_path = '/Users/zhangjiawei/Pictures/hupu_photo'
# for pic_url in sub_pic_url_list:
#     r = requests.get(pic_url, stream=True, timeout=10)
#     pic = pic_path + '/' + str(number) + '.jpg'
#     number = number + 1
#     with open(pic, 'w') as f:
