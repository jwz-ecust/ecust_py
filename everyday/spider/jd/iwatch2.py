import requests
import time
import json
import os
from bs4 import BeautifulSoup

user = "aaronzjw"
password = "Cbbzjw140308"

jd = 'https://passport.jd.com/uc/login'
s = requests.session()
data = {
    "loginname": user,
    "nloginpwd": password,}


req = s.get(jd)
soup = BeautifulSoup(req.text, "html.parser")
items = soup.select("form#formlogin > input")
uuid = items[0].get('value').encode('utf-8')
data['uuid'] = uuid
input_name = items[-1].get('name').encode("utf-8")
input_value = items[-1].get("value").encode("utf-8")
data[input_name] = input_value
verify_url = "http:" + soup.find("img", id="JD_Verification1")["src2"] + "&yys=" + str(int(time.time()*1000))
print(verify_url)
img = s.get(verify_url)
f = open("./zjw.jpg", "wb")
f.write(img.content)
authcode = input()
data["authcode"] = authcode
print(data)

posreq = s.post("https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F", data=data)
posreq.encoding = "gbk"
with open("./cookiefile", "w") as f:
    json.dump(s.cookies.get_dict(), f)
