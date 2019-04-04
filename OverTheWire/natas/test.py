import requests
from requests.auth import HTTPBasicAuth

# Just for a nicer output
from phpserialize import loads

uri = 'http://natas26.natas.labs.overthewire.org/'

payload = {'x1' : '10', 'y1' : '10', 'x2' : '140', 'y2' : '140'}
p = requests.get(uri,
    auth=HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'),
    cookies={'PHPSESSID' : 'umphack'},
    params = payload)
payload = {'x1' : '150', 'y1' : '150', 'x2' : '10', 'y2' : '10'}
p = requests.get(uri,
    auth=HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'),
    cookies={'PHPSESSID' : 'umphack',
             'drawing': p.cookies['drawing']},
    params = payload)
payload = {'x1' : '5', 'y1' : '10', 'x2' : '10', 'y2' : '20'}
p = requests.get(uri,
    auth=HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'),
    cookies={'PHPSESSID' : 'umphack',
             'drawing': p.cookies['drawing']},
    params = payload)
print( loads(p.cookies['drawing'].decode('base64')) )
# print( loads(p.cookies['drawing'].decode('base64')) )

# g = requests.get(uri,
#     auth=HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'),
#     cookies={'PHPSESSID' : 'umphack'},
#     data = Data)
# print( g.text )
