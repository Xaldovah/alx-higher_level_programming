#!/usr/bin/python3
import math


class MagicClass:
    """
    Represents a magical class that performs calculations on circles.

    Attributes:
        __radius (float): The radius of the circle.

    Methods:
        __init__: Initializes a MagicClass object with the given radius.
        area(self): Calculates and returns the area of the circle.
        circum(self): Calculates and returns the circumference of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a MagicClass object with the given radius.

        Args:
            radius (float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 2 * math.pi * self.__radius

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return math.pi * self.__radius * 2
