#!/usr/bin/python3

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as respons:
        body = respons.read()
        print(f"Body response:$")
        print(f"    - type: {type(body)}$")
        print(f"    - content: {body}$")
        print(f"    - utf8 content: {body.decode('utf8')}$")
