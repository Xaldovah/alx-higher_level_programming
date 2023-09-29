#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(req) as r:
        content = r.read()
        utf8_content = content.decode('utf-8')

        print('Body response:')
        print('\t- type:', type(content))
        print('\t- content:', content)
        print('\t- utf8 content:', utf8_content)
