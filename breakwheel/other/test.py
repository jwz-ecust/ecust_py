import eventlet
from eventlet.green import urllib2


urls = [
    "http://eventlet.net/doc/examples.html",
    "http://www.jianshu.com/subscriptions#/subscriptions/1115945/collection",
    "http://www.jianshu.com/p/a6f9c9cc05fa",
    "http://www.codexiu.cn/python/blog/824/",
    "http://www.voidcn.com/blog/u010571844/article/p-4971982.html"
]


def fetch(url):
    print "opening: ", url
    body = urllib2.urlopen(url).read()
    print "done with ", url
    return url, body


pool = eventlet.GreenPool(200)

for url, body in pool.imap(fetch, urls):
    print "got body from ", url, " of length ", len(body)