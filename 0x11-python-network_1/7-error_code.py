#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8)

Usage: 7-error_code.py <URL>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
