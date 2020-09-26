#!/usr/bin/env python3

import requests
import hashlib
from datetime import datetime
import re

url = 'http://docker.hackthebox.eu:32303/'
date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
headers = {
  'Connection': 'keep-alive',
  'Origin': 'http://docker.hackthebox.eu:32303',
  'Cache-Control': 'max-age=0',
  'Upgrade-Insecure-Requests': '1',
  'DNT': '1',
  'Content-Type': 'application/x-www-form-urlencoded',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Referer': 'http://docker.hackthebox.eu:32303/',
  'Accept-Language': 'nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7',
  # 'Cookie': '_ga=GA1.2.2044974768.1599477793; _gid=GA1.2.293204667.1599477793; ajs_anonymous_id=%22d0e4756a-1a8e-4d24-95bd-c41dd6c14357%22; ajs_user_id=%2287c57cc720760f163edeae4b044530f5%22; __auc=4724042d17468e5e227dba69d95; PHPSESSID=i316sld8rjd38j8i19njn7msu3',
  "Date": date, # Forbidden header
  # "Early-Data": "1",
}

resp = requests.get(url, headers=headers)
html = resp.content.decode('utf8')
print(resp.cookies)
print(html)

# while True:
match = re.search(r"<h3 align='center'>(.*)<\/h3>", html)
if match:
    string = match.group(1)
    md5 = hashlib.md5(string.encode('ascii')).hexdigest()
    resp = requests.post(url, data={'hash': md5},
                         headers=headers,
                         cookies=resp.cookies)
    # date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    html = resp.content.decode('utf8')
    print(html)
        # if not re.search('Too slow!', html):
        #     break
