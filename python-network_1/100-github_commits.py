#!/usr/bin/python3
"""
Script to fetch and print recent commits from a GitHub repository
"""

import requests
import sys

def fetch_commits(repo_name, owner_name):
    """
    Fetches recent commits from a GitHub repository

    Args:
        repo_name (str): The name of the repository
        owner_name (str): The owner of the repository

    Returns:
        list: A list of tuples containing the SHA and author name of the recent commits
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        return [(commit.get('sha'), commit.get('commit').get('author').get('name')) for commit in commits[:10]]
    else:
        print(f"Error: Failed to fetch commits, Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    commits = fetch_commits(repo_name, owner_name)
    for sha, author_name in commits:
        print(f"{sha}: {author_name}")

