#!/usr/bin/python3
"""Python script that takes in a URL and an email address"""
import requests
from sys import argv


if __name__ == "__main__":
    email_dt = {'email': argv[2]}
    req = requests.post(argv[1], data=email_dt)

    print(req.text)
