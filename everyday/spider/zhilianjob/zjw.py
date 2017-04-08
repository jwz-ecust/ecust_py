# -*- coding: utf-8 -*-
import json


f = open("zjw.txt", 'w')
zjw = json.load(open("./items.json"))
# print dir(zjw)
for i in zjw:
    # print type(i)
    # print i
    print i['job_position'].encode("utf-8")
    f.write(i[u'job_position'].encode("utf-8") + ' ' + i[u'job_company'].encode("utf-8") + ' ' + i[u'job_date'].encode("utf-8") + ' ' + i[u'job_name'].encode("utf-8") + ' ' + str(i[u'job_price']) + "\n")
