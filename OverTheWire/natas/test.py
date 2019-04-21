#!/usr/bin/env python3

import requests, string
import base64
from requests.auth import HTTPBasicAuth
from urllib.parse import unquote

uri = 'http://natas28.natas.labs.overthewire.org/index.php'
username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

# chars = ''.join([string.digits, string.ascii_letters])

for i in range(32):
    Data = {'query' : 'A'*i + 'B' * (i+4)}

    # params = '&'.join(['%s=%s' % (k, v) for k, v in Data.items()])
    # for i in chars:
    # query = {'query' : i}
    p = requests.post( uri,
        auth=HTTPBasicAuth(username, password),
        # data = Data)
        params = Data)
    # print( '\n'.join( p.text.split('\r\n')[24:]) + '\n\n' )
    # print( unquote(p.url.split('=')[1]) )
    resp = p.url.split("query=")[1]
    print( len(base64.b64decode(unquote(resp).encode('utf8'))) )
    print( len(base64.b64decode(unquote(resp))) )

# f = open('./query.txt')
# lines = [line.rstrip('\n') for line in f]
# query = [k.split('\t') for k in lines]
# queries = [''.join([v[2],v[3],v[4]]) for v in query]
# f.close()

# for q in queries:
#     # g = q + ''
#     # str(q).encode('base64')
#     print( str(q[4:-3]).decode('base64') )

