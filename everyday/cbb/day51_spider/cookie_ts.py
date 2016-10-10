# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import re

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({'userint':'Y11140001'})
url = "http://59.78.108.52/WebUI/login.aspx"
result = opener.open(url,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
find_url='http://59.78.108.52/webxs/webxs_kccjPrint.asp?userid=40958&deptid=1&usertype=s&identity=31204066'

result = opener.open(find_url)
response = result.read()
response = unicode(response,'GBK').encode('UTF-8')
print response
