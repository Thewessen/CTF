#!/usr/bin/env python3

import requests, string
import base64
from requests.auth import HTTPBasicAuth
from urllib.parse import unquote

uri = 'http://natas28.natas.labs.overthewire.org/index.php'
username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

chars = ''.join([string.digits, string.ascii_letters])


# params = '&'.join(['%s=%s' % (k, v) for k, v in Data.items()])
# print(params)
for i in chars:
    Data = {'query' : i}
#     Data = {'query' : i,
#             'table' : 'users',
#             'username': 'natas' + i}
    p = requests.post( uri,
            auth=HTTPBasicAuth(username, password),
            # data = Data)
            params = Data)
        # json = '{' + ', '.join(['%s : %s' % (k, v) for k, v in Data.items()]) + '}'
    query =  p.url.split('=')[1]
    print( base64.b64decode(unquote(query)) )
# print( '\n'.join( p.text.split('\r\n')[24:]) + '\n\n' )

# f = open('./query.txt')
# lines = [line.rstrip('\n') for line in f]
# query = [k.split('\t') for k in lines]
# queries = [''.join([v[2],v[3],v[4]]) for v in query]
# f.close()

# for q in queries:
#     print( base64.b64decode(unquote(q).decode('utf8')) ) 

