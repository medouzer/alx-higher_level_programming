#!/usr/bin/python3
"""Time for an interview!"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits?per_page=10"
    # headers = {'Authorization': 'Bearer {}'.format(password)}
    req = requests.get(url).json()
    for i in req:
        print(f"{i.json().get('sha')}: ", end="")
        print(f"{i.json().get('commit').get('author').get('name')}")
