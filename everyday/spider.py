# -*- coding: utf-8 -*-
import urllib2
import io
import random
import urllib
from bs4 import BeautifulSoup
import re
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def getHtml(url):
    #尽可能让爬虫显示为一个正常用户。若不设置，则发送的请求中，user-agent显示为Python+版本
    user_agent = [
        'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
        'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
        'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)'
    ]
    #设置网页编码格式，解码获取到的中文字符
    encoding = "gb18030"
    #构造http请求头，设置user-agent
    header = {"User-Agent":random.choice(user_agent)}
    #构造发送请求
    request = urllib2.Request(url,headers=header)
    #发送请求，获取服务器响应回来的html页面
    html = urllib2.urlopen(request).read()
    #使用beautifulSoup处理的html页面，类似dom
    soup = BeautifulSoup(html,from_encoding=encoding)
    return soup

# 获取整个站点所有图集的页码
def getPageNum(url):
    soup = getHtml(url)
    # 直接在站点首页获取所有图集的总页码
    nums=soup.find_all('a',class_='page-numbers')
    # 除掉“下一页”的链接，并获取到最后一页
    totlePage = int(nums[-2].text)
    return totlePage

#获取指定页面下图集名称和链接
def getPicNameandLink(url):

    soup = getHtml(url)
    meun = []
    #类似html dom对象，直接查找id为“pins”的ul标签，返回的结果是一个dom对象
    targetul = soup.find("ul",id="pins")
    if targetul:
        #获取该ul下所有的超链接，返回值的类型是list，find_all中第二个参数表示某个指定标签的属性
        pic_list = targetul.find_all("a",target="_blank")
        if pic_list:
           # 遍历所有指定的标签a
            for pic in pic_list:
                #获取图集的链接
                link = pic["href"]
                picturename = ""
                #找到标签a中，“class”为“lazy”的img标签。
                #find中，第二个参数表示某个指定标签的属性。
                #在python中class是保留字，所有标签的class属性的名称为“class_”
                img = pic.find("img",class_='lazy')
                if img:
                    # 保证中文字符能够正常转码。
                    picturename = unicode(str(img["alt"]))
                else:
                    continue
                #插入图集名称和对应的url
                meun.append([picturename,link])

        return meun
    return None

#function获取所有的图集名称
def getallAltls(url):
    totalpage = getPageNum(url)
    #获取首页中所有的图集名称。首页的url和其他页面不同，没有page
    meun = getPicNameandLink(url)
    #循环遍历所有的图集页面，获取图集名称和链接
    for pos in range(2,totalpage):
        currenturl = url + "/page/" + str(pos)
        #getPicNameandLink()返回的值是一个list。
        #当一个list插入到另一个list中时，使用extend。
        #若是插入一个值时，可以用append
        meun.extend(getPicNameandLink(currenturl))

    return meun

# 获取从首页到指定页面所有的图集名称和链接
def getparAltls(url,page):
    meun = getPicNameandLink(url)

    for pos in range(2,page):
        currenturl = url + "/page/" + str(pos)
        meun.extend(getPicNameandLink(currenturl))

    return meun

#获取单个相册内图片页码
def getSinglePicNum(url):
    soup = getHtml(url)
    #pagenavi还是一个对象（Tag），可以通过find_all找出指定标签出来
    pagenavi = soup.find("div",class_="pagenavi")
    pagelink = pagenavi.find_all("a")

    num = int(pagelink[-2].text)
    return num


#下载单个相册中的所有图片
def getSinglePic(url,path):
    totalPageNum = getSinglePicNum(url)
    #从第一页开始，下载单个图集中所有的图片
    #range()第二个参数是范围值的上限，循环时不包括该值
    #需要加1以保证读取到所有页面。
    for i in range(1,totalPageNum + 1):
        currenturl = url + "/" + str(i)
        downloadpic(currenturl,path)

#下载单个页面中的图片
def downloadpic(url,path):
    soup = getHtml(url)
    #找出指定图片所在父容器div
    pageimg = soup.find("div",class_="main-image")

    if pageimg:
        #找出该div容器中的img，该容器中只有一个img
        img = pageimg.find("img")
        #获取图片的url
        imgurl = img["src"]
        #获取图片的文件名
        restring = r'[A-Za-z0-9]+\.jpg'
        reimgname = re.findall(restring,imgurl)

        #将图片保存在指定目录下
        path = str(path)
        if path.strip() == "":
            downloadpath = reimgname[0]
        else:
            downloadpath = path + "/" + reimgname[0]
        #伪装一下下载的http请求，否则有些站点不响应下载请求。
        #不设置的话，下载请求中的user-agent为python+版本号
        urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
        #下载图片到指定目录中，保留图片在服务器上的文件名
        urllib.urlretrieve(imgurl,downloadpath)

def downimgofsite(url,path = ""):

    path = str(path)
    #获取所有图集的名称和链接
    meun_list = getallAltls(url)
    directorypath = ""

    for meun in meun_list:
        directoryname = meun[0]
        if path.strip() != "":
            directorypath = path + "/" + directoryname
        else:
            directorypath = os.getcwd + "/" + directoryname

        if not os.path.exists(directorypath):
            os.makedirs(directorypath)

        getSinglePic(meun[1], directorypath)


if __name__ == "__main__":
    page = 8
    url = "http://photo.hupu.com"
    menu = getallAltls(url)
    #menu = getparAltls(url, page)

    f = open("tsts.txt","a")
    for i in menu:
        f.write(str(unicode(i[0]))+"\t"+str(i[1])+"\n")
    f.close()