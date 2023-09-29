#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')

    with urlopen(req) as r:
        content = r.read()
        utf8_content = content.decode('utf-8')

        print('Body response:')
        print('    - type:', type(content))
        print('    - content:', content)
        print('    - utf8 content:', utf8_content)
