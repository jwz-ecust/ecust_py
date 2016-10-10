# -*- coding: utf-8 -*-

import urllib2
import re

class DoubanSpider(object):
    def __init__(self):
        self.page = 1
        self.cur_url = "http://movie.douban.com/top250?start={page}&filter=&type="
        self.datas = []
        self._top_num = 1
        print "豆瓣电影爬虫就绪,准备爬去数据..."

    def get_page(self,cur_page):
        url = self.cur_url
        try:
            my_page = urllib2.urlopen(url.format(cur_page-1)).read().decode("utf-8")
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print "The server couldn't fulfill the request"
                print "Error code: %s" % e.code()
            elif hasattr(e,"reason"):
                print "We failed to reach a server. Please check your url and read the Reason"
                print "Error reason: %s" % e.reason()
        return my_page

    def find_title(self, my_page):

        temp_data = []
        movie_items = re.findall(r'<span.*?class="title">(.*?)</span>',my_page,re.S)
        for index, item in enumerate(movie_items):
            if item.find("&nbsp") == -1:
                temp_data.append("Top"+str(self._top_num)+" "+item)
                self._top_num += 1
        self.datas.extend(temp_data)

    def start_spider(self):
        while self.page<=4:
            my_page = self.get_page(self.page)
            self.find_title(my_page)
            self.page+=1

def main():
    a = "1"
    print a
    myspider = DoubanSpider()
    print dir(myspider)
    myspider.start_spider()
    for item in myspider.datas:
        print item
    print "豆瓣爬虫爬去结束..."