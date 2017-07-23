import requests

ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
header = {"User-Agent": ua}
url = "http://twin.sci-hub.bz/captcha/securimage_show.php"

for i in range(8914, 10000):
    req = requests.get(url, headers=header)
    open("./captcha/{}.jpg".format(str(i)), "wb").write(req.content)
