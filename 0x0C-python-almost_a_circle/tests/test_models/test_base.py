#!/usr/bin/python3
"""import modules"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8


class TestBaseClass(unittest.TestCase):
    """Test the class Base"""

    @classmethod
    def setUp(cls):
        """setUp"""
        Base._Base__nb_objects = 0
        pass

    @classmethod
    def tearDown(cls):
        """tearDown"""
        pass

    def test_pep8(self):
        """
        Test that the code conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(
                ['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0, "Pep8 Error in file")

    def test_is_private(self):
        """Test that nb_objects is private."""
        print("__nb_object is private")
        self.assertTrue(hasattr(Base, "_Base__nb_objects"), 0)

    def test_id_1(self):
        """Test the id attribute of Base."""
        base1 = Base()
        self.assertEqual(base1.id, 1)

    def test_id_2(self):
        """Test the id attribute of Base."""
        base_instance_1 = Base(12)
        base_instance_2 = Base()
        self.assertEqual(base_instance_1.id, 12)
        self.assertEqual(base_instance_2.id, 1)

    def test_float(self):
        """Test the float overflow"""
        base1 = Base(float("inf"))
        self.assertEqual(base1.id, float("inf"))

    def test_string(self):
        """Test the string"""
        base1 = Base("test")
        self.assertEqual(base1.id, "test")

    def test_to_json_string(self):
        """Test the to_json_string method"""
        rect1 = Rectangle(4, 6, 2, 8)
        list_dict = rect1.to_dictionary()
        json_dict = Base.to_json_string([list_dict])
        self.assertEqual(str(type(json_dict)), "<class 'str'>")

    def test_to_json(self):
        """Test the to_json method"""
        dict1 = {"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}
        dict2 = {"id": 2, "width": 4, "height": 5, "x": 1, "y": 2}
        json_string = Base.to_json_string([dict1, dict2])
        jload = json.loads(json_string)
        self.assertEqual(jload, [dict1, dict2])
        self.assertTrue(isinstance(json_string, str))

    def test_from_json_to_str(self):
        """Test the from_json_string method"""
        json_t = '[{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]'
        json_str = Base.from_json_string(json_t)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertTrue(isinstance(json_str, list))

    def test_to_json_none(self):
        """Test the to_json_string method"""
        json1 = Base.to_json_string(None)
        self.assertEqual(json1, "[]")


if __name__ == '__main__':
    unittest.main()
