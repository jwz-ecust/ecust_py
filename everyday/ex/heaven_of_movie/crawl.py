# -*- coding: utf-8 -*-
from lxml import etree
import re
import os
import threading
from urllib2 import Request, urlopen


class mythread(threading.Thread):   # 继承父类threading.Thread
    def __init__(self, url, new_dir, crawledurls):
        threading.Thread.__init__(self)
        self.url = url
        self.new_dir = new_dir
        self.crawledurls = crawledurls

    def run(self):                  # 把要执行的代码写到run函数里面, 线程在创建后会直接运行run函数
        print "starting running!"
        CrawListPage(self.url, self.new_dir, self.crawledurls)

start_url = "http://www.ygdy8.com/index.html"
host = "http://www.ygdy8.com"


# 判断地址是否已经爬取


def __isexit(newurl, crawledurls):
    if newurl in crawledurls:
        return True
    else:
        return False


# 获取页面资源
def __getpage(url):
    req = Request(url)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    req.add_header("User-Agent", user_agent)
    try:
        response = urlopen(req, timeout=60)
    except:
        return "error"
        pass
    else:
        page = response.read()
        return page


# 处理资源页面, 爬去资源地址
def CrawlSourcePage(url, filedir, filename, crawledurls):
    print url
    page = __getpage(url)
    if page == "error":
        return
    crawledurls.append(url)
    page = page.decode('gbk','ignore')
    tree = etree.HTML(page)
    nodes = tree.xpath("//div[@align='left']//table//a")
    try:
        source = filedir + "/" + filename + ".txt"
        f = open(source.decode("utf-8"),'w')
        for node in nodes:
            sourceurl = node.xpath("text()")[0]
            f.write(sourceurl.encode("utf-8"), 'w')
        f.close()
    except:
        print "not found!!!!!!"


# 解析分类文件
def CrawListPage(indexurl, filedir, crawledurls):
    print "正在解析分类主页资源"
    print indexurl
    page = __getpage(indexurl)
    if page == "error":
        return
    crawledurls.append(indexurl)
    page = page.decode('gbk','ignore')
    tree = etree.HTML(page)
    nodes = tree.xpath("//div[@class='co_content8']//a")
    for node in nodes:
        url = node.xpath("@href")[0]
        if re.match(r"/",url):
            # 非分页地址,可以从中解析出视频资源地址
            if __isexit(host + url, crawledurls):
                pass
            else:
                # 文件名是不能出现已下特殊符号
                filename = node.xpath("text()")[0].encode("utf-8").replace("/", " ")\
                                                                  .replace("\\", " ")\
                                                                  .replace(":", " ")\
                                                                  .replace("*", " ")\
                                                                  .replace("?", " ")\
                                                                  .replace("\"", " ")\
                                                                  .replace("<", " ") \
                                                                  .replace(">", " ")\
                                                                  .replace("|", " ")
                CrawlSourcePage(host+url, filedir, filename, crawledurls)
            pass
        else:
            # 分页地址 从嵌套中再次解析
            print "分页地址, 从嵌套中再次解析",url
            index = indexurl.rfind("/")
            baseurl = indexurl[0:index+1]
            pageurl = baseurl + url
            if __isexit(pageurl, crawledurls):
                pass
            else:
                print "分页地址 从中嵌套再次解析",pageurl
                CrawListPage(pageurl, filedir, crawledurls)
            pass
    pass


# 解析首页


def craw_index_page(starturl):
    print "正在爬取首页"
    page = __getpage(starturl)
    if page == "error":
        return
    page = page.decode('gbk', 'ignore')
    tree = etree.HTML(page)
    nodes = tree.xpath("//div[@id='menu']//a")
    print "首页解析出地址", len(nodes), "条"
    for node in nodes:
        crawledurls = []
        crawledurls.append(starturl)
        url = node.xpath("@href")[0]
        if re.match(r"/html/[A-Za-z0-9_/]+/index.html", url):
            if __isexit(host+url, crawledurls):
                pass
            else:
                print host+url
                try:
                    catalog = node.xpath("text()")[0].encode("utf-8")
                    new_dir = "/Users/zhangjiawei/Documents/new/"+catalog
                    os.makedirs(new_dir.decode("utf-8"))
                    print "创建分类目录成功--------"+new_dir
                    print host+url
                    thread = mythread(host+url, new_dir, crawledurls)
                    thread.start()
                except:
                    pass
craw_index_page(start_url)
