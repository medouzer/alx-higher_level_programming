#!/usr/bin/python3
"""What's my status? #0"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as respons:
        body = respons.read()
        print(f"Body response:$\n\t- type: {type(body)}$\n\t- content: {body}$")
        print(f"\t- utf8 content: {body.decode('utf8')}$")
