# -*- coding: utf-8 -*-

import urllib
from urllib2 import Request, urlopen, URLError

username = '10100346'
password = 'zjw865614'
data = {
    'TxtStudentId': username,
    'TxtPassword': password,
    '__VIEWSTATE': '/wEPDwUJMTg2MzE1NTYyD2QWAgIBD2QWAgIGDw8WAh4EVGV4dAVQ5a2m55Sf5Yid5aeL5a+G56CB5Li66Lqr5Lu96K+B5Y+\
    35ZCO5YWt5L2N44CC5a+G56CB6ZW/5bqm5LiN6LaF6L+HMTDkuKrlrZfnrKbjgIJkZGTItFe6UDnNqdE2sz592HXKwZ7Fhw==',
    '__EVENTVALIDATION':'/wEWBALplYnsCgK/ycb4AQLVqbaRCwLi44eGDNL1/UVfta6zTJ9DMRXMNe6Ao6Wm'
}
data = urllib.urlencode(data)

try:
    req = Request("http://202.120.108.14/ecustedu/K_StudentQuery/K_Default.aspx")
    response = urlopen(req, data, timeout=10)
    content = response.read()
    response.close()
except URLError, e:
    if hasattr(e, 'reason'):
        info = '[ERROR] Failed to reach the server. \n Reason:' + str(e.reason)
    elif hasattr(e, 'code'):
        info = "[ERROR] The server couldn\'t fullfill the request. \nError code:"
    else:
        info = "[ERROR] Unknown URLError"
    print info
except Exception:
    import traceback
    print "Generic exception: " + traceback.format_exc()