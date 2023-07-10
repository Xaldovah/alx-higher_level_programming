#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
