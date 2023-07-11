#!/usr/bin/python3
"""import module"""

from json import dumps
"""save_to_json_file function module"""


def save_to_json_file(my_obj, filename):
    """save_to_json_file function"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
