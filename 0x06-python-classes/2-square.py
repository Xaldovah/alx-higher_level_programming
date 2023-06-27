#!/usr/bin/python3
"""Square Class

A Square Class

"""


class Square:

    def __init__(self, size=0):
        """__init__

        The __init__ method initializes the size value of the square.
        """

        if type(size) is not int:
            """Attributes:
                size: This is the size of the square
            """
            raise TypeError("size must be an integer")
            """Raise:
                TypeError: Is raised if size type is not `int`
            """

        if size < 0:
            raise ValueError("size must be >= 0")
            """Raise:
                ValueError: Is raised if size is less than 0
            """

        self.__size = size
