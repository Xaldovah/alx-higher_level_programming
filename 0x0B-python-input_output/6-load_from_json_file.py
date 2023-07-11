#!/usr/bin/python3
"""import module"""

from json import loads
"""load_from_json_file function module"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file” function"""
    with open(filename, "r", encoding="utf-8") as f:
        return loads(f.read())
