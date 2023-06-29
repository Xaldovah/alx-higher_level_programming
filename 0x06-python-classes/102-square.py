#!/usr/bin/python3

class Square:
    """
    Square Class
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int or float): The size value to set.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Overloads the == operator to compare the areas of two squares.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Overloads the != operator to compare the areas of two squares.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Overloads the > operator to compare the areas of two squares.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if area is equal or less than square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Overloads the >= operator to compare the areas of two squares.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if area is equal or less than square, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Overloads the < operator to compare the areas of two squares.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if area is equal or less than square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Overloads the <= operator to compare the areas of two squares.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if area is equal or less than square, False otherwise.
        """
        return self.area() <= other.area()
