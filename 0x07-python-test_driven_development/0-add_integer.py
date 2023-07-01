#!/usr/bin/python3

"""
This module provides a function for adding integers or floats.

- add_integer(a, b=98): Adds two integers or floats
"""


def add_integer(a, b=98):
    """
    Add two integers.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = to_int(a)
    b = to_int(b)
    return a + b


def to_int(num):
    """
    Converts a float to an integer if necessary.

    Parameters:
    - num: A number to be converted.

    Returns:
    The integer representation of `num` if `num` is a float,
    otherwise returns `num` unchanged.

    Example:
    >>> to_int(10.5)
    10
    >>> to_int(7)
    7
    """
    if type(num) is float:
        num = int(num)
    return num
