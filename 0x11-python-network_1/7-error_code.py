#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(argv[1])

    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
