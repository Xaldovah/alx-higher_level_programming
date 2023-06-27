#!/usr/bin/python3
"""Square Class

A Square Class

"""


class Square:

    def __init__(self, size=0):
        """__init__

        The __init__ method initializes the size value of the square.

        Attributes:
            size (:obj:int, optional): The size of the square.

        Raises:
            TypeError: Is raised if size type is not `int`.

            ValueError: Is raised if size is less than 0.

        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
