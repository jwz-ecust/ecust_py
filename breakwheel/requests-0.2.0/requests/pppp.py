from core import Request

url = "http://www.baidu.com"
zjw = Request()
zjw.url = url
zjw.method = "POST"
print zjw
print zjw._checks()

print zjw._get_opener()

zjw.send()
print zjw.response
print zjw.headers
print zjw.response.status_code
print zjw.response.content