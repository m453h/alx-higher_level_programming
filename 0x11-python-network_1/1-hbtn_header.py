#!/usr/bin/python3
"""This script displays the value of the X-Request-Id

Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))