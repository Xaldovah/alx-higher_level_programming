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

    """func that prints in stdout the square with the character #"""
    def my_print(self):
        """check if size is equal to 0"""
        if self.__size == 0:
            """if true print new line"""
            print()
            """and return none"""
            return None

        """if not zero start a loop"""
        for i in range(1, self.area() + 1):
            """print the character # with no new line"""
            print("#", end="")

            """if the modulo is equal to zero and i greater than 0"""
            if i % self.__size == 0 and i > 0:
                """print a new line"""
                print()
