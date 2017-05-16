from core import get
import urllib2

url = "http://www.baidu.com"
response = get(url)

print response.url
print response.content