# -*- coding: utf-8 -*-
import requests

url = "http://i1.hoopchina.com.cn/u/1611/11/391/3589391/61f7e673gif.gif"
html = requests.get(url)
with open("./zjw.gif", "wb") as fuck:
    fuck.write(html.content)
