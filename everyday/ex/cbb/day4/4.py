# coding=utf-8
import re


with open('1.html', 'rb') as f:
    data = f.read()


data = data.replace('\r', '').replace('\b', '').replace('\n', '')
find = re.compile(r'href="(.*?)"')
result = find.findall(data)
with open('zjw.txt', 'w') as f:
    for i in result:
        i += '\n'
        f.writelines(i)
