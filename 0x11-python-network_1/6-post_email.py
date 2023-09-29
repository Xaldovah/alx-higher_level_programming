#!/usr/bin/python3
"""Python script that takes in a URL and an email address"""
import requests
from sys import argv


if __name__ == "__main__":
    dt = {'email': argv[2]}
    r = requests.post(argv[1], data=dt)
    print("Your email is:", r.text)
