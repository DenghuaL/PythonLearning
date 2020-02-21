#!usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request


req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for v,k in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))



import json

def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
        return json.loads(data)

# 测试
URL = 'https://yesno.wtf/api'
data = fetch_data(URL)
print(data)
#assert data['answer']== 'yes' and (data['forced']== False)
print('ok')