#!/usr/bin/python3
"""class Student module"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json method"""
        return self.__dict__

    def to_json(self, attrs=None):
        """to_json method"""
        if type(attrs) is list:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """reload_from_json method"""
        self.__dict__ = json
