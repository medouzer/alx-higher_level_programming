#!/usr/bin/python3
"""What's my status? #1"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    print(req)
