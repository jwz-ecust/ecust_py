# -*- coding: utf-8 -*-
# @Date    : 2017-03-15 02:34:48
# @Author  : "zhangjiawei"
# @Email  : "aaronzjw@icloud.com"
# @Link    : ${https://github.com/jwz-ecust}
# @Version : $Id$

import requests
from bs4 import BeautifulSoup
# import time

main_url = "http://t66y.com/"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"

header = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Cookie": "__cfduid=dfa4a65f4db9ac0d20b5ada789cea6e3d1489516084; UM_distinctid=15ace9c3b012ce-00749031f2b8b1-1c3e6b52-fa000-15ace9c3b0240d; CNZZDATA950900=cnzz_eid%3D1709133675-1489520571-%26ntime%3D1489520927; PHPSESSID=oj2mi102el4db8sioehrpehcn7",
    "Host": "t66y.com",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0"
}

# source_url = "http://t66y.com/thread0806.php?fid=16&search=&page=2"

s = requests.Session()
proxies = {
    "http": "http://127.0.0.1:8087",
    "https": "http://127.0.0.1:8087"
}
n = 1
for i in range(2):
    source_url = "http://t66y.com/thread0806.php?fid=16&search=&page={}".format(str(i))

    sreq = s.get(url=source_url, proxies=proxies, headers=header, verify=False)
    print sreq.content.decode("ISO-8859-1")
    ssoup = BeautifulSoup(sreq.content.decode("ISO-8859-1"), "html.parser")
    cbb = ssoup.find_all("td", class_="tal")
    for i in cbb:
        sub_url = "http://t66y.com/" + i.h3.a.get('href')
        print sub_url
        if not sub_url.endswith(".html"):
            continue
        req = s.get(url=sub_url, proxies=proxies, headers=header, verify=False)
        soup = BeautifulSoup(req.content.decode("ISO-8859-1"), "html.parser")
        zjw = soup.find_all("div", class_="tpc_content")
        print zjw
        for i in zjw:
                br = i.br
                if br is not None:
                    inputs = br.find_all('input')
                    for j in inputs:
                        print u"================准备下载第{}张图片================".format(str(n))
                        purl = j.get('src')
                        print purl
                        n += 1
                        filename = purl.split("/")[-1]
                        ppath = "./" + filename
                        with open(ppath, "wb") as fuck:
                            image = requests.get(purl, stream=True, headers=header, verify=False).content
                            fuck.write(image)

