#!/usr/bin/python3

"""Square Class"""


class Square:
    """__init__ initializes size value of the square."""
    def __init__(self, size=0):
        """Attributes: size: size of the square"""
        if type(size) is not int:
            """if size is not int raise TypeError"""
            raise TypeError("size must be an integer")
        """check if size is less than 0"""
        if size < 0:
            """if size is less than 0 raise ValueError"""
            raise ValueError("size must be >= 0")
        """self.size = size"""
        self.size = size

    """Decorator"""
    @property
    def size(self):
        """return the private instance"""
        return self.__size

    """Setter"""
    @size.setter
    def size(self, size):
        """check if size is an int"""
        if type(size) is not int:
            """if not int raise a TypeError"""
            raise TypeError("size must be an integer")
        """check if size is less than 0"""
        if size < 0:
            """if size is less than 0 raise a ValueError"""
            raise ValueError('size must be >= 0')

        """Assign value to private instance size"""
        self.__size = size

    """define area func to calc the area of the square"""
    def area(self):
        """Return the current square area"""
        return self.__size ** 2
