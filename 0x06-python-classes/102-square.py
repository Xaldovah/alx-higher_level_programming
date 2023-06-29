#!/usr/bin/python3
"""Square Class"""


class Square:
    """__init__ Initializes the Square instance"""
    def __init__(self, size=0):
        """Assign value to size"""
        self.size = size

    """Getter method for the size attributes"""
    @property
    def size(self):
        """Returns: int: The size of the square"""
        return self.__size

    """Setter method for the size attribute."""
    @size.setter
    def size(self, value):
        """Checks if value is a number"""
        if not isinstance(value, (int, float)):
            """if not raises TypeError message"""
            raise TypeError("size must be a number")
        """Checks if value is less than 0"""
        if value < 0:
            """if not raises ValueError message"""
            raise ValueError("size must be >= 0")
        """Assigns value to size"""
        self.__size = value

    """Calculates and returns the area of the square"""
    def area(self):
        """Returns: float: The area of the square"""
        return self.__size ** 2

    """Overloads the == operator to compare the areas of two squares"""
    def __eq__(self, other):
        """Returns: bool: True if the areas are equal, False otherwise"""
        return self.area() == other.area()

    """Overloads the != operator to compare the areas of two squares"""
    def __ne__(self, other):
        """Returns: bool: True if the areas are not equal, False otherwise"""
        return self.area() != other.area()

    """Overloads the > operator to compare the areas of two squares"""
    def __gt__(self, other):
        """Returns: bool: True if area equal or less than square, or False"""
        return self.area() > other.area()

    """Overloads the >= operator to compare the areas of two squares."""
    def __ge__(self, other):
        """Returns: True if area is equal or less than square, or False"""
        return self.area() >= other.area()

    """Overloads the < operator to compare the areas of two squares"""
    def __lt__(self, other):
        """Returns: True if area is equal or less than square, or False"""
        return self.area() < other.area()

    """Overloads the <= operator to compare the areas of two squares"""
    def __le__(self, other):
        """Returns: True if area is equal or less than square, or False"""
        return self.area() <= other.area()
