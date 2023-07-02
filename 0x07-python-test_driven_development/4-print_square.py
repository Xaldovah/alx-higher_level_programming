#!/usr/bin/python3

"""Square Printing Module

This module provides a function to print a square of hashes with a given size.
"""


def print_square(size):
    """
    Prints a square of hashes with the given size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.

    Examples:
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####

        >>> print_square(3)
        ###
        ###
        ###

        >>> print_square(1)
        #

        >>> print_square(0)
        ValueError: size must be >= 0

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
