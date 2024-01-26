#!/usr/bin/python3
"""Response header value #1"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    info = req.headers.get("X-Request-Id")
    print(info)
