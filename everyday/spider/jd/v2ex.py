# -*- coding: utf-8 -*-
'''
可以登录v2ex
'''

import requests
from bs4 import BeautifulSoup

url = "http://www.v2ex.com/signin"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
header = {"User-Agent": UA, "Referer": "http://www.v2ex.com/signin"}

v2_s = requests.Session()

f = v2_s.get(url, headers=header)
soup = BeautifulSoup(f.content, "html.parser")
once = soup.find('input', {"name": "once"})["value"]
print(once)


postdat = {
    "65a51164612b7fe6e7e695189f7318b08a6e651fc303bb90e8debf17fa55e0d9": "aaronzjw",
    "16aff65da5cc399bca115dd40027baa59c4c9df04ef8ef657ee65f13b99e8422": "zjw865614",
    "once": once,
    "next": "/"
}

v2_s.post(url, data=postdat, headers=header)

f = v2_s.get("https://www.v2ex.com/settings", headers=header)
print(f.content.decode())
