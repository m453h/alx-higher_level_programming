#!/usr/bin/python3
"""
This script  takes in a URL,
sends a request to the URL and,
displays the value of the X-Request-Id
"""
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(dict(response.headers).get("X-Request-Id"))
