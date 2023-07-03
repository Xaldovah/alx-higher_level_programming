#!/usr/bin/python3

"""Rectangle Class"""


class Rectangle:
    """
    Initialize the private attributes of width and height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the printable representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for i in range(self.__height))

    def __repr__(self):
        """Return the string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
