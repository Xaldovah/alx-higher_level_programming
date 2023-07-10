#!/usr/bin/python3
"""MyList class module that inherits from list"""


class MyList(list):
    """inherits from the class list"""
    def print_sorted(self):
        """prints sorted list"""
        if issubclass(MyList, list):
            print(sorted(self))
