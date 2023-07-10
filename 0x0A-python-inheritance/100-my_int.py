#!/usr/bin/python3
"""MyInt class module that inherits from int class"""


class MyInt(int):
    """MyInt class that inherits from int class"""
    def __eq__(self, value):
        """check if equal"""
        return int(self) != int(value)

    def __ne__(self, value):
        """check if not equal"""
        return int(self) == int(value)
