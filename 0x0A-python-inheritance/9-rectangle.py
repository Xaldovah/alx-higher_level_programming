#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area()"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator()"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """__init__()"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area()"""
        return self.__width * self.__height

    def __str__(self):
        """__str__()"""
        return f"[Rectangle] {self.__width}/{self.__height}"
