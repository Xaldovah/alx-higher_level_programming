#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """inherits_from"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
