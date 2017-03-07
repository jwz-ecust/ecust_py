# -*- coding: utf-8 -*-
import urllib2
import re
'''
5xx服务器错误:
这类状态码代表了服务器在处理请求的过程中有错误或者异常状态发生，也有可能是服务器意识到以当前的软硬件资源无法完成对请求的处理。除非这是一个HEAD请求，否则服务器应当包含一个解释当前错误状态以及这个状况是临时的还是永久的解释信息实体。浏览器应当向用户展示任何在当前响应中被包含的实体。
这些状态码适用于任何响应方法。
500 Internal Server Error
服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般來說，這個問題都會在伺服器的程序碼出錯時出現。
501 Not Implemented
服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。
502 Bad Gateway
作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
503 Service Unavailable
由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。如果能够预计延迟时间，那么响应中可以包含一个Retry-After头用以标明这个延迟时间。如果没有给出这个Retry-After信息，那么客户端应当以处理500响应的方式处理它。
作为网关或者代理工作的服务器尝试执行请求时，未能及时从上游服务器（URI标识出的服务器，例如HTTP、FTP、LDAP）或者辅助服务器（例如DNS）收到响应。
注意：某些代理服务器在DNS查询超时时会返回400或者500错误。
505 HTTP Version Not Supported
服务器不支持，或者拒绝支持在请求中使用的HTTP版本。这暗示着服务器不能或不愿使用与客户端相同的版本。响应中应当包含一个描述了为何版本不被支持以及服务器支持哪些协议的实体。
506 Variant Also Negotiates
由《透明内容协商协议》（RFC 2295）扩展，代表服务器存在内部配置错误：被请求的协商变元资源被配置为在透明内容协商中使用自己，因此在一个协商处理中不是一个合适的重点。
507 Insufficient Storage
服务器无法存储完成请求所必须的内容。这个状况被认为是临时的。（WebDAV RFC 4918）
509 Bandwidth Limit Exceeded
服务器达到带宽限制。这不是一个官方的状态码，但是仍被广泛使用。
510 Not Extended
获取资源所需要的策略并没有被满足。（RFC 2774）
'''


def download(url, user_agent='wswp', num_retries=2):
    print "starting downloading======>", url
    headers = {'User_agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP error
                return download(url, num_retries - 1)
    return html


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall("<loc>(.*?)</loc>", sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here
        # ...

# 获取伯乐在线的所有文章
map = 'http://python.jobbole.com/sitemap.xml'

html = download(map)
links = re.findall("<loc>(.*?)</loc>", html)
print len(links)
for i in links:
    print i
