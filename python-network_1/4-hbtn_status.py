#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using requests"""
import requests

if __name__ == "__main__":
    """Fetches https://alu-intranet.hbtn.io/status using requests"""
    r = requests.get('https://alu-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
