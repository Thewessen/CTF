#!/usr/bin/env python3

import requests
from base64 import urlsafe_b64decode
import jwt
import re
import sys

url = 'http://docker.hackthebox.eu:32476'
secret = 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw' # ??
output = 'output.txt'

def main():
    resp = requests.get(url)
    text = f'{url} ({resp.status_code})\n'
    if resp.status_code != 200:
        print(text)
        return

    n = re.search(r'\d+(?=\<\/h1\>)', resp.content.decode('utf-8')).group(0)

    session = resp.cookies.get('session')
    text += f'session: {session}\n'
    # print(decoded)
    try:
        header = jwt.get_unverified_header(session)
        text += f'header: {header}\n'

        ingredient = urlsafe_b64decode(header['ingredient'][' b'])
        measurements = urlsafe_b64decode(header['measurements'][' b'])
        text += f'ingredient: {ingredient}\n'
        text += f'measurements: {measurements} and output {n}\n'
        if exec(f'{measurements} != {n}'):
            text += 'NOT EQUAL\n'
    except Exception as e:
        text += e.args[0]

    with open(output, 'a+') as f:
        f.write(text + '\n')

if __name__ == '__main__':
    main()
