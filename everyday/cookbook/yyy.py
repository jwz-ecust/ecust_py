import re
import urllib.request
import urllib


def getImageUrls(page):
    # req = urllib.request.Request(url)

    url_index = 'http://www.meizitu.com/a/%s.html' % page
    url_open = urllib.request.urlopen(url_index)
    html = url_open.read()
    html = html.decode('gbk')
    image_index = r'src="(.*?\.jpg)"'
    imgre = re.compile(image_index)
    image_list = re.findall(imgre, html)
    x = 0
    for imgurl in image_list:
        req = urllib.request.Request(imgurl)
        req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
        response = urllib.request.urlopen(req)
        print(x, imgurl)
        open("{}.jpg".format(str(x)), "wb").write(response.read())
        # urllib.request.urlretrieve(imgurl, './%s.jpg' % str(x))
        x += 1

if __name__ == '__main__':
    page = input('Please input your page to download:')
    # page = "11"
    getImageUrls(page)
