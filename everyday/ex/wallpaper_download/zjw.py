import requests
import re
import pickle
import json


from bs4 import BeautifulSoup

url = 'http://muchong.com/bbs/'
login_url = 'http://muchong.com/bbs/logging.php?action=login'

header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
}
login_data ={
    'email':'aaronzjw',
    'password':'zjw897978644',
    'rememberme':'true',
    '_discuz_cc':'55641288695675615',
    '_emuch_index':'1',
    '_ga':'GA1.2.1866848510.1468328084',
    '_gat':'1',
    'last_ip':'210.51.42.144_1435017',
    'mc_sid':'4YlK40YdlfyfS7nz',
}

s = requests.session()
s.post(login_url,headers=header,data=login_data)
print s.text

print s.cookies