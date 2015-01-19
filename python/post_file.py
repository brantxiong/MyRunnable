# -*- coding: utf-8 -*-
import requests
url = 'http://httpbin.org/post'
files = {'file': open('a.txt', 'rb')}
values = {'author': 'John Smith'}
r = requests.post(url, files=files, data=values)
print r.content