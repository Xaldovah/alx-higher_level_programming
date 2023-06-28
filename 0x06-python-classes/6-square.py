#!/usr/bin/python3

"""Square Class"""


class Square:
    """__init__ initializes size value of the square."""
    def __init__(self, size=0, position=(0, 0)):
        """Attributes: size: size of the square"""
        if type(size) is not int:
            """if size is not int raise TypeError"""
            raise TypeError("size must be an integer")
        """check if size is less than 0"""
        if size < 0:
            """if size is less than 0 raise ValueError"""
            raise ValueError("size must be >= 0")

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
    def position(self, position):
        """check the tuple position if false"""
        if self.__tuple(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__indexes(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__integers(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__values(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")

        """Assign value to the private instance position"""
        self.position = position

    """tuple def with one arg"""
    def __tuple(self, position):
        """check if the type of pos is tuple"""
        if type(position) is tuple:
            """return true if yes"""
            return True
        """return false if no"""
        return False

    """indexes def with one arg"""
    def __indexes(self, position):
        """check if the len of pos is equal to 2"""
        if len(position) == 2:
            """return true if yes"""
            return True
        """return false if no"""
        return False

    """integers def with one arg"""
    def __integers(self, position):
        """check if the type of pos is int"""
        if type(position[0]) is int and type(position[1]) is int:
            """return true if yes"""
            return True
        """return false if no"""
        return False

    """values def with one arg"""
    def __values(self, position):
        """check if pos[0] and pos[1] is greater than 0"""
        if position[0] >= 0 and position[1] >= 0:
            """return true if yes"""
            return True
        """return false if no"""
        return False

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
        """check if pos is greater than 0"""
        if self.__position[1] > 0:
            """Enter loop"""
            for i in range(self.__position[1]):
                """print empty spaces"""
                print("")
        """enter j loop"""
        for j in range(1, self.area() + 1):
            """if modulo is equal to 1"""
            if j % self.__size == 1:
                """print"""
                print("{:>{w}}".format("#", w=self.__position[0] + 1), end="")
            else:
                print("#", end="")
                """if modulo is equal to 0 and j is greater than 0"""
                if j % self.__size == 0 and j > 0:
                    """print new line"""
                    print()
