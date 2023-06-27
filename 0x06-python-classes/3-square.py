#!/usr/bin/python3
""" Square Class """


class Square:
    """__init__ initialise the size"""

    def __init__(self, size=0):
        """checks if size is an integer"""
        if type(size) is not int:
            """if not integer print a TypeError message"""
            raise TypeError("size must be an integer")
            """checks if size is less than 0"""
        if size < 0:
            """if it is less than 0, print ValueError message"""
            raise ValueError("size must be >= 0")
        """Assign value to size"""
        self.__size = size
    """Area def that will contain the square of area"""
    def area(self):
        """Return square of the area"""
        return self.__size ** 2
