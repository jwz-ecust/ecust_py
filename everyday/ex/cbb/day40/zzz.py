# -*- coding:utf-8 -*-
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    # items = re.findall(pattern,content)
    for item in content.split('\n'):
        haveImg = re.search("img", item)
        if not haveImg:
            print item
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
