#!/usr/bin/python3
"""This script takes GitHub credentials (username and password)
and uses the GitHub API to display the user id

Usage: ./10-my_github.py <username> <password>
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    try:
        print(response.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
