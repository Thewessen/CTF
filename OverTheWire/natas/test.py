#!/usr/bin/env python3

import requests, string
from requests.auth import HTTPBasicAuth

uri = 'http://natas28.natas.labs.overthewire.org/'
username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

query = {'query' :
        'd"'}

# Create a username natas28 with 64 trailing spaces, the 1 gets trunked and the
# spaces trimed
Data = {'username' : "natas28" + " "*64 + "1",'password' : "1"}

chars = ''.join([string.digits, string.ascii_letters])

Data = {'query' : "b"}

p = requests.get( uri,
        auth=HTTPBasicAuth(username, password),
        # data = Data)
        params = query)
print( '\n'.join( p.text.split('\r\n')[24:]) + '\n\n' )
