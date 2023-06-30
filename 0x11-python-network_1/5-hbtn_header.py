#!/usr/bin/python3
"""This script displays the value of the X-Request-Id

Usage: ./5-hbtn_header.py <URL>
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
