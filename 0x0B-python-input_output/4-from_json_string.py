#!/usr/bin/python3
"""import module"""

from json import loads
"""from_json_string function module"""


def from_json_string(my_str):
    """
    returns an object (Python data structure)
    represented by a JSON string
    """
    return (loads(my_str))
