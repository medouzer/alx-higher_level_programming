#!/usr/bin/python3
"""My GitHub!"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {"Authorization": f"Bearer {password}"}
    req = requests.get(url, headers=headers)
    print(req.json())
