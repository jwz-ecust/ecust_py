# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import datetime

r = requests.get('https://book.douban.com')
html = r.text

soup = BeautifulSoup(html, 'html.parser')
items = []

global_nav_items = soup.find('div', class_='global-nav-items')

for tag in global_nav_items.find_all('a'):
    items.append(tag.string)


class Info(object):

    def __init__(self, title, img, link, author, year, publisher, abstract):
        self.title = title
        self.img = img
        self.link = link
        self.author = author
        self.year = year
        self.publisher = publisher
        self.abstract = abstract


new_book_html = soup.find(
    'ul', class_='list-col list-col5 list-express slide-item')

book_info_list = []

for tag in new_book_html.find_all('li'):
    info_html = tag.find('div', class_='info')
    info_title = info_html.find('a')
    title = info_title.string.strip().encode('utf-8')
    # print title
    cover = tag.find('div', class_='cover')
    img = cover.find('img')['src'].strip().encode('utf-8')
    # print img
    href = info_title['href'].strip().encode('utf-8')
    author = info_html.find(class_='author').string.strip().encode('utf-8')
    year = info_html.find(class_='year').string.strip().encode('utf-8')
    publisher = info_html.find(
        class_='publisher').string.strip().encode('utf-8')
    abstract = info_html.find(class_='abstract').string.strip().encode('utf-8')
    book = Info(title, img, href, author, year, publisher, abstract)
    book_info_list.append(book)


def save():
    today = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
    file_name_1 = 'Douban-' + today + '-recommended-book'
    path = '/Users/zhangjiawei/Code/myblog/source/_posts/'
    # file_name = file_name_1 + '.md'
    file_name = path + file_name_1 + '.md'
    with open(file_name, 'w') as file:
        file.write('---\n')
        file.write('title: ' + file_name_1 + '\n')
        file.write('date: ' + today + '\n')
        file.write('tag: ' + '\'' + 'douban-book' + '\'' + '\n')
        file.write('---\n')
    with open(file_name, 'a') as file:
        num = 1
        for book in book_info_list:
            file.write('\n\n')
            file.write('##' + str(num) + '.' + book.title)
            file.write('\n')
            file.write(
                '![' + book.title + ' cover img](' + book.img + ')')
            file.write('\n\n')
            file.write('简介\n')
            file.write('---\n')
            file.write(book.abstract)
            file.write('\n\n')
            file.write('作者:       ' + book.author + '\n\n')
            file.write('出版时间:    ' + book.year + '\n\n')
            file.write('出版社:      ' + book.publisher + '\n\n')
            file.write('[更多...](' + book.link + ')')
            num += 1

if __name__ == '__main__':
    save()
