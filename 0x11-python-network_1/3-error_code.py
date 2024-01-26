#!/usr/bin/python3
"""Error code #0"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as respons:
            de_respons = respons.read().decode('utf-8')
            print(de_respons)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e}")