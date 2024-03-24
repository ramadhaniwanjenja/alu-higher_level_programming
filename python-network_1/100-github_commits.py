#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""
import sys
import requests

if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        r = requests.get(url)
        r.raise_for_status()  # Raise an error if request fails
        json_o = r.json()
        for commit in json_o:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
    except Exception as e:
        print("Error:", e)
