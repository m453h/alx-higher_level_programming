#!/usr/bin/python3
"""This script takes GitHub credentials (username and password)
and uses the GitHub API to display the user id

Usage: ./100-github_commits.py <repository> <owner>
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    response = requests.get(url)
    try:
        commits = response.json()
        i = 0
        for commit in commits:
            if i > 9:
                break
            print("{}: {}".format(commit.get("sha"),
                                  commit.get("commit").
                                  get("author").
                                  get("name")))
            i += 1
    except ValueError:
        print("Not a valid JSON")
