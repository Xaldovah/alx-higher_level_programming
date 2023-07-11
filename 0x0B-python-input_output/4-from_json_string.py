#!/usr/bin/python3
"""import module"""

from json import dumps
"""from_json_string function module"""


def from_json_string(my_str):
    """
    returns an object (Python data structure)
    represented by a JSON string
    """
    return (dumps(eval(my_str)))
