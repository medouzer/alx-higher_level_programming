#!/usr/bin/python3
"""My GitHub!"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = f"https://api.github.com/user/{username}"
    headers = {'Authorization':'Bearer {}'.format(password)}
    req = requests.get(url, headers=headers)
    print(req.json())
