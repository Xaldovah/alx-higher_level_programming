#!/usr/bin/python3
"""import modules"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8


class TestSquareClass(unittest.TestCase):
    """Test the class Square"""

    @classmethod
    def setUp(cls):
        """setUp"""
        Base._Base__nb_objects = 0
        cls.sqr1 = Square(1, 3)
        cls.sqr2 = Square(1, 3, 5)
        cls.sqr3 = Square(1, 3, 5, 7)
        cls.sqr4 = Square(1, 3, 5, 7, 9)

    @classmethod
    def tearDown(cls):
        """tearDown"""
        pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors \
                (and warnings).")

    def test_is_subclass(self):
        """Test that Square is a subclass of Base."""
        self.assertTrue(issubclass(Square, Base))

    def test_instance(self):
        """Test that Square is an instance of Base."""
        self.assertIsInstance(self.sqr1, Base)
        self.assertIsInstance(self.sqr2, Base)
        self.assertIsInstance(self.sqr3, Base)
        self.assertIsInstance(self.sqr4, Base)

    def test_values(self):
        """Test the values of Square."""
        sqr1 = Square(1)
        self.assertEqual(sqr1.size, 1)

    def test_str(self):
        """Test the str method of Square."""
        sqr1 = Square(2)
        sqr2 = Square(3, 4, 5)
        self.assertEqual(str(sqr1), '[Square] (2) 0/0 - 2')
        self.assertEqual(str(sqr2), '[Square] (3) 4/5 - 3')

    def test_area(self):
        """Test the area method of Square."""
        sqr1 = Square(2)
        self.assertEqual(sqr1.area(), 4)

    def test_save_to_file(self):
        """Test the save_to_file method of Square."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_load_file(self):
        """Test the save_to_file and load_from_file methods of Square."""
        sqr1 = Square(4, 6, 2, 8)
        sqr2 = Rectangle(7, 9)
        Square.save_to_file([sqr1, sqr2])
        load_file = Square.load_from_file()
        self.assertEqual(isinstance(load_file, list))

    def test_to_dict(self):
        """Test the to_dict method of Square."""
        dict1 = self.sqr1.to_dictionary()
        self.assertEqual({"id": 1, "size": 2, "x": 3, "y": 0}, dict1)
        self.assertEqual(isinstance(dict1, dict))

    def test_class(self):
        """Test the class of Square."""
        self.assertTrue(str(Square), "<class 'models.square.Square'>")

    def test_zero(self):
        """Test the zero of Square."""
        sqr1 = Square(4)
        with self.assertRaises(ValueError):
            sqr1.size = 0

    def test_negative(self):
        """Test the negative of Square."""
        sqr1 = Square(6)
        with self.assertRaises(ValueError):
            sqr1.size = -5
