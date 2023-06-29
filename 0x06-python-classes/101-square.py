#!/usr/bin/python3

"""Square Class"""


class Square:
    """__init__ initializes size value of the square."""
    def __init__(self, size=0, position=(0, 0)):
        """Assign value to size"""
        self.size = size
        """Assign value to position"""
        self.position = position

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
        """Assign value"""
        self.__size = size

    """decorator"""
    @property
    def position(self):
        """return the private instance"""
        return self.__position

    """position setter"""
    @position.setter
    def position(self, value):
        """check the if value and tuple are integers or value is not 2"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        """Assign value to position"""
        self.__position = value

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
            """and return"""
            return
        """check if pos is greater than 0"""
        if self.__position[1] > 0:
            """Enter loop"""
            for i in range(self.__position[1]):
                """print empty spaces"""
                print()
        """enter j loop"""
        for j in range(1, self.area() + 1):
            """if modulo is equal to 1"""
            if j % self.__size == 1:
                """print"""
                print(" " * self.__position[0], end="")
            print("#", end="")
            """if modulo is equal to 0 and j is greater than 0"""
            if j % self.__size == 0 and j > 0:
                """print new line"""
                print()
