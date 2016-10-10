# -*- coding: utf-8 -*-
import requests
import re

'''
首先，我们准备好了和 Chrome 一致的 HTTP 请求头部信息。
具体来说，其中的 User-Agent 是比较重要的。
而后，仿照浏览器与服务器的通信，我们创建了一个 requests.Session。
接着，我们用 GET 方法打开登录页面，并用正则库解析到 authenticity_token。
随后，将所需的数据，整备成一个 Python 字典备用。
最后，我们用 POST 方法，将表单提交到 session 接口。
最终的结果也是符合预期的：经由 302 跳转，打开了（200）GitHub 首页。
'''
cs_url = 'https://github.com/login'
cs_urer = 'aaronzjw6@gmail.com'
cs_psw = 'Cbbzjw140308'
my_headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

sss=requests.session()
r = sss.get(cs_url,headers=my_headers)

reg = r'<input name="authenticity_token" type="hidden" value="(.*)" />'
pattern = re.compile(reg)
result = pattern.findall(r.content)
token = result[0]

mydata = {
    'commit':'Sign in',
    'utf8':'%E2%9C%93',
    'authenticity_token':'token',
    'login':cs_urer,
    'password':cs_psw
}

cs_url = 'http://github.com/session'
r = sss.post(cs_url,headers=my_headers,data=mydata)
print r.url, r.status_code, r.history