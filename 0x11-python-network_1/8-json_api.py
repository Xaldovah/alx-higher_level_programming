#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    try:
        url = 'http://0.0.0.0:5000/search_user'
        data = {'q': q}
        r = requests.post(url, data).json()

        if {'id', 'name'} <= r.keys():
            print('[{id}] {name}'.format(id=r.get('id'), name=r.get('name')))
    else:
        print('No result')
    except ValueError:
        print('Not a valid JSON')
