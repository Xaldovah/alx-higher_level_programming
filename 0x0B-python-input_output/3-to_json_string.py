#!/usr/bin/python3
"""import module"""

from json import dumps
"""to_json_string function module"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return dumps(my_obj)
