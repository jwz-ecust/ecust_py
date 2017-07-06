import requests

url = "https://www.github.com"
auth = requests.AuthObject('request', 'request')
req = requests.get(url,
                   headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Mobile Safari/537.36"},
                   auth=auth)
print req.status_code
print req.headers
