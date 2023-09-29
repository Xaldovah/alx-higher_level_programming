#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = Request(argv[1])

    try:
        with urlopen(url) as r:
            print(r.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
