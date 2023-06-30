#!/usr/bin/python3
"""This script sends a POST request to the passed URL with email parameter,
and displays the body of the response

Usage: ./8-json_api.py <search_parameter>
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": q})
    try:
        response = response.json()
        if response == {}:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
