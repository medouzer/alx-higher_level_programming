#!/usr/bin/python3
"""Time for an interview!"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    # headers = {'Authorization': 'Bearer {}'.format(password)}
    req = requests.get(url)
    for i in range(10):
        print(f"{req.json()[i].get('sha')}: ", end="")
        print(f"{req.json()[i].get('commit').get('author').get('name')}")
