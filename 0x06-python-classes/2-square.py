#!/usr/bin/python3
"""Square Class

A Square Class

"""


class Square:
    """__init__ method initializes the size value of the square."""
    def __init__(self, size=0):
        """Attributes: size: This is the size of the square"""
        if type(size) is not int:
            """Raise: TypeError: Is raised if size type is not `int`"""
            raise TypeError("size must be an integer")
        """Check if size is than `0`"""
        if size < 0:
            """Raise: ValueError: Is raised if size is than `0`"""
            raise ValueError("size must be >= 0")
        """size: data assigning"""
        self.__size = size
