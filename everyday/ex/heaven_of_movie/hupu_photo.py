import os
import re
from lxml import etree
import threading
import urllib2


hupu_url = "http://photo.hupu.com"


def __get_page(url):
    req = urllib2.Request(url)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
                 '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    req.add_header("User-Agent", user_agent)
    try:
        response = urllib2.urlopen(req, timeout=60)
    except:
        return "get page error"
    else:
        page = response.read()
        return page


content = __get_page(hupu_url).decode('gbk', 'ignore')
tree = etree.HTML(content)