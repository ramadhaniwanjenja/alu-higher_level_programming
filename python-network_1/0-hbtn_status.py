#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status
"""

import urllib.request

def fetch_status():
    """
    Fetches the status from https://alu-intranet.hbtn.io/status
    """
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode("utf-8"))

if __name__ == "__main__":
    fetch_status()

