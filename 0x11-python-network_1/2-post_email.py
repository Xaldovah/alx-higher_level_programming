#!/usr/bin/python3
"""takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urlencode({'email': email}).encode('ascii')

    req = Request(url, data)
    with urlopen(req) as r:
        body = r.read().decode('utf-8')
        print(body)
