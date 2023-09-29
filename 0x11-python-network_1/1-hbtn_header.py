#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value"""
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    url = sys.argv[1]

    with urllib.request.urlopen(url) as r:
        x_req_id = r.info().get('X-Request-Id')
        print(x_req_id)
