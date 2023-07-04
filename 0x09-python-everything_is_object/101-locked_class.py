#!/usr/bin/python3
"""LockedClass class module"""


class LockedClass(object):
    """Restricts new instances except first_name"""
    __slots__ = 'first_name'
