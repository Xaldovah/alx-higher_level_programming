#!/usr/bin/python3
import math

"""
    Represents a magical class that performs calculations on circles.
"""


class MagicClass:
    """Initializes a MagicClass object with the given radius."""
    def __init__(self, radius):
        """Args:
            radius (float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """Calculates and returns the area of the circle."""
    def area(self):
        """Returns: float: The area of the circle."""
        return 2 * math.pi * self.__radius

    """Calculates and returns the circumference of the circle."""
    def circumference(self):
        """Returns: float: The circumference of the circle."""
        return math.pi * self.__radius * 2
