import urllib2
response = urllib2.urlopen('http://www.51buy.com/')
print response.geturl()
print response.info()