#!/usr/bin/env python2

import os
import debug

os.environ['FLASK_APP'] = 'debug.py'

client = debug.app.test_client()
resp = client.get('/')
cookie = resp.headers.get('Set-Cookie')
token = cookie.split(';')[0].split('=')[1]
print(token)

print(resp.data)
