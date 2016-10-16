import urllib2

url="http://photo.hupu.com"
request = urllib2.urlopen(url)
with open('hupu_photo.html','w') as f:
    f.writelines(request.read())