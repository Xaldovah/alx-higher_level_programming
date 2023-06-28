#!/usr/bin/python3
import dis
import math

"""MagicClass"""


class MagicClass:
    """__init__ initialize and have attributes"""
    def __init__(self, radius=0):
        """Assign value to radius"""
        self.__radius = 0
        """check if type is neither an int or a float"""
        if type(radius) is not int and type(radius) is not float:
            """If true raise a TypeError"""
            raise TypeError("radius must be a number")
        """Assign value to radius"""
        self.__radius = radius
    """area def"""
    def area(self):
        """return calc"""
        return self.__radius ** 2 * math.pi
    """circumference def"""
    def circumference(self):
        """return the calc"""
        return 2 * math.pi * self.__radius
