import requests
import re

url = "http://muchong.com/bbs/logging.php?action=login"
sess = requests.session()

# 构建headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 \
        Safari/537.36'}

#  第一次请求 get -->获取参数 formhash
r1 = sess.get(url, headers=headers)
# 获取 formhash 可以写成函数复用
content1 = r1.text
formhash = re.findall(r'<input type="hidden" name="formhash" value="(.*?)">',
                      content1)[0]
data = {
    'formhash': None,
    'username': 'aaronzjw',
    'password': 'zjw897978644',
    'cookietime': '31536000',
    'loginsubmit': '%B5%C7%C2%BD%D0%A1%C4%BE%B3%E6'}
data['formhash'] = formhash

# 第二次请求 post --> 获取问题并解答以及参数post_sec_hash
r2 = sess.post(url, data=data, headers=headers)
content2 = r2.text
question = re.findall(r'<div style="padding:10px 0;">问题：(.*?)\?<br>',
                      content2)[0]
post_sec_hash = re.findall(
    r'<input type="hidden" name="post_sec_hash" value="(.*?)" >',
    content2)[0]

operations = {'减': '-', '加': '+', '除以': '/', '乘以': '*'}
for name, op in operations.items():
    if name in question:
        spq = question.split(name)[:2]
        num1, num2 = spq[0], spq[1].split("等于")[0]
        answer = eval("{} {} {}".format(num1, op, num2))

login_data = {
    'formhash': formhash,
    'post_sec_code': str(answer),
    'post_sec_hash': post_sec_hash,
    'username': 'aaronzjw',
    'loginsubmit': '%CC%E1%BD%BB'}

# 第三次请求, 登陆
r3 = sess.post(url, data=login_data, headers=headers)
r3_cookie = r3.cookies.get_dict()

# 请求主页
# my = sess.get("http://muchong.com/bbs/space.php?uid=1435017",
#    cookies=r3_cookie)
# print(my.text)

# 第四次post请求，获取金币, requests 默认会带上cookies
get_credit = "http://muchong.com/bbs/memcp.php?action=getcredit&uid=1435017"
getcredit_data = {
   'formhash': '2005901a',
   'getmode': '2',
   'message': '',
   'creditsubmit': '%C1%EC%C8%A1%BA%EC%B0%FC'}

credit = sess.post(get_credit, data=getcredit_data)
print("Done! Get the credit!")
