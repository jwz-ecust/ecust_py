import urllib2
url = 'http://59.78.108.52/webxs/webxs_kccjPrint.asp?userid=40969&deptid=1&usertype=s&identity=31204077'
res = urllib2.urlopen(url)
print unicode(res.read(),'GBK').encode('UTF-8')
