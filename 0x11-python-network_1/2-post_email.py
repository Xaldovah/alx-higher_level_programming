#!/usr/bin/python3
"""takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if len(sys.argv) < 3:
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

dt = urllib.parse.urlencode({'email': email}).encode('utf-8')

req = urllib.request.Request(url, dt)
with urllib.request.urlopen(req) as r:
    body = r.read().decode('utf-8')
    print(body)
