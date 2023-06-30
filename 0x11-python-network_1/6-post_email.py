#!/usr/bin/python3
"""This script sends a POST request to the passed URL with email parameter,
and displays the body of the response

Usage: ./6-post_email.py <URL> <email>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    response = requests.post(url, data=data)
    print(response.text)
