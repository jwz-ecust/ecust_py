import requests
import re
import pickle
import json


from bs4 import BeautifulSoup

url = 'http://172.20.13.100'
url_login = 'http://172.20.13.100/gw.html?url=emuch.net'


login_data = {
    'username':'Y11140009',
    'password':'zjw865614',
}

header ={'Accept': '*/*'
'Accept-Encoding': 'gzip, deflate'
'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36
X-Requested-With: XMLHttpRequest
}


s = requests.session()
s.post(url_login)