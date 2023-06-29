#!/usr/bin/python3
"""import the math module"""

import math
"""MagicClass Class"""


class MagicClass:
    """__init__ Initializes the class object with the given radius."""
    def __init__(self, radius):
        """Assign value to radius"""
        self.__radius = 0
        """Check if type of radius is not an int or a float"""
        if type(radius) is not int and type(radius) is not float:
            """if yes raise the appropriate error message"""
            raise TypeError("radius must be a number")
        """Assign value to radius"""
        self.__radius = radius

    """Calculates and returns the area of the circle."""
    def area(self):
        """Returns: float: The area of the circle."""
        return 2 * math.pi * self.__radius

    """Calculates and returns the circumference of the circle."""
    def circumference(self):
        """Returns: float: The circumference of the circle."""
        return math.pi * self.__radius * 2
