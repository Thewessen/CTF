#!/usr/bin/env python3

import requests, string
from requests.auth import HTTPBasicAuth

uri = 'http://natas28.natas.labs.overthewire.org/index.php'
username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

# chars = ''.join([string.digits, string.ascii_letters])

Data = {'query' : 'b',
        'user' : 'admin'}

params = '&'.join(['%s=%s' % (k, v) for k, v in Data.items()])
print(params)
# for i in chars:
# query = {'query' : i}
p = requests.get( uri,
    auth=HTTPBasicAuth(username, password),
    # data = Data)
    params = params)
print( '\n'.join( p.text.split('\r\n')[24:]) + '\n\n' )
# print( p.url.split('=')[1] )

# f = open('./query.txt')
# lines = [line.rstrip('\n') for line in f]
# query = [k.split('\t') for k in lines]
# queries = [''.join([v[2],v[3],v[4]]) for v in query]
# f.close()

# for q in queries:
#     # g = q + ''
#     # str(q).encode('base64')
#     print( str(q[4:-3]).decode('base64') )

