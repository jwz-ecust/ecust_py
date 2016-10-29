# -*- coding: utf-8 -*-
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
try:
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    content = response.read()
    print content
    pattern = re.compile(
        '<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
        'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div \
        class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[3])
        if not haveImg:
            print item[0], item[1], item[2], item[3], item[4]
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason
