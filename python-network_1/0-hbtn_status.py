#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
            utf8_content = html_content.decode('utf-8')

            print("Body response:")
            print("\t- type:", type(html_content))
            print("\t- content:", html_content)
            print("\t- utf8 content:", utf8_content)
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code, e.reason, file=sys.stderr)
