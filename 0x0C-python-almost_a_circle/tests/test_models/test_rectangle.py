#!/usr/bin/python3
"""import modules"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8


class TestRectangleClass(unittest.TestCase):
    """Test the class Rectangle"""

    @classmethod
    def setUp(cls):
        """setUp"""
        Base._Base__nb_objects = 0
        cls.rect1 = Rectangle(1, 3)
        cls.rect2 = Rectangle(1, 3, 5)
        cls.rect3 = Rectangle(1, 3, 5, 7)
        cls.rect4 = Rectangle(1, 3, 5, 7, 9)

    @classmethod
    def tearDown(cls):
        """tearDown"""
        pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Pep8 Error in file")

    def test_is_subclass(self):
        """Test that Rectangle is a subclass of Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_instance(self):
        """Test that Rectangle is an instance of Base."""
        self.assertIsInstance(self.rect1, Base)
        self.assertIsInstance(self.rect2, Base)
        self.assertIsInstance(self.rect3, Base)
        self.assertIsInstance(self.rect4, Base)

    def test_save_to_file(self):
        """Test the save_to_file method of Rectangle"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_load_file(self):
        """Test the save_to_file and load_from_file methods of Rectangle"""
        rect1 = Rectangle(4, 6, 2, 8)
        rect2 = Rectangle(7, 9)
        Rectangle.save_to_file([rect1, rect2])
        load_file = Rectangle.load_from_file()
        self.assertEqual(isinstance(load_file, list))

    def test_to_dict(self):
        """Test the to_dict method of Rectangle."""
        dict1 = self.rect1.to_dictionary()
        self.assertEqual(
            {"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}, dict1)

    def test_class(self):
        """Test the class of Rectangle."""
        self.assertTrue(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_area(self):
        """Test the area method of Rectangle."""
        rect1 = Rectangle(10, 10, 10, 10, 42)
        self.assertEqual(str(rect1), "[Rectangle] (42) 10/10 - 10/10")

    def test_update(self):
        """Test the update method of Rectangle."""
        rect1 = {"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}
        rect2 = {"id": 2, "width": 4, "height": 5, "x": 1, "y": 2}
        rect_create1 = Rectangle.create(**rect1)
        rect_create2 = Rectangle.create(**rect2)
        self.assertEqual("[Rectangle] (1) 0/0 - 2/3", str(rect_create1))
        self.assertEqual("[Rectangle] (2) 1/2 - 4/5", str(rect_create2))
        self.assertTrue(isinstance(rect1, dict))
        self.assertTrue(isinstance(rect2, dict))

    def test_save_to_file(self):
        """Test the save_to_file method of Rectangle"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_load_file(self):
        """Test the save_to_file and load_from_file methods of Rectangle"""
        rect1 = Rectangle(4, 6, 2, 8)
        rect2 = Rectangle(7, 9)
        Rectangle.save_to_file([rect1, rect2])
        load_file = Rectangle.load_from_file()
        self.assertEqual(isinstance(load_file, list))

    def test_args(self):
        """Test the args method of Rectangle."""
        with self.assertRaises(TypeError):
            rect1 = Rectangle()
            self.rect1.area(1)

    def test_id(self):
        """Test the id method of Rectangle."""
        rect1 = Rectangle(1, 2)
        self.assertEqual(rect1.id, 1)
        rect2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(rect2.id, 2)
