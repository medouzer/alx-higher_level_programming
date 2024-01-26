#!/usr/bin/python3
"""Search API"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data={'q': q})
    try:
        data_json = req.json()
        if data_json:
            print(f"[{data_json['id']}] {data_json['name']}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
