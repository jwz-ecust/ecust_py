import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def extract_image(text):
    soup = BeautifulSoup(text)
    elems = soup.find_all("div",{'class':'subhead'})
    return [elem.get("img src") for elem in elems]

def main(url):
    html = get_html(url)
    img_urls = extract_image(html)
    print  '\n'.join(img_urls)

if __name__ == "__main__":
    main('http://bbs.hupu.com/16693560.html')