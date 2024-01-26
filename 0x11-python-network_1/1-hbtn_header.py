#!/usr/bin/python3
"""Response header value #0"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        info = response.info()
        print(f"info: {info}")
