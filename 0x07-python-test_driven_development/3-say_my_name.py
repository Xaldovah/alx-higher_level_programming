#!/usr/bin/python3

"""Name Printing Module"""


def say_my_name(first_name, last_name=""):
    """
    Prints the given first name and last name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed. Defaults to "".

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe

        >>> say_my_name("Alice")
        My name is Alice

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
