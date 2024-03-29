#!/usr/bin/python3
"""import modules"""
import json
import csv
from os import path
"""Base class module"""


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string([obj.to_dictionary()
                        for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string"""
        list_to_dict = []
        if list_objs is not None:
            list_objs = []
        for items in list_objs:
            list_to_dict.append(items.to_dictionary())

        with open("{}.csv".format(cls.__name__), "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""
        instanceList = []
        try:
            with open("{}".format(cls.__name__), "r", encoding="utf-8") as f:
                objectList = cls.from_json_string(f.read())
        except IOError:
            return []
        for dictionary in objectList:
            instanceList.append(cls.create(**dictionary))
        return instanceList
