#!/usr/bin/python3
import unittest
import json
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""
TestSquareClass module
"""


class TestSquareClass(unittest.TestCase):
    """
    TestSquareClass contains unit tests for the Square class.
    """

    @classmethod
    def setUp(cls):
        """
        Set up class method.
        """
        Base._Base__nb_objects = 0
        cls.sqr1 = Square(2, 4)
        cls.sqr2 = Square(2, 4, 6)
        cls.sqr3 = Square(2, 4, 6, 8)
        cls.sqr4 = Square(2, 4, 8, 10)

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method.
        """
        pass

    def test_class(self):
        """
        Tests if Square is a class.
        """
        self.assertTrue(str(Square), "<class 'models.square.Square'>")

    def test_values(self):
        """
        Tests square values.
        """
        sqr1 = Square(3)
        self.assertEqual(sqr1.size, 3)

    def test_str(self):
        """
        Tests square string representation.
        """
        sqr1 = Square(3)
        sqr2 = Square(4, 5, 6)
        self.assertEqual(sqr1.__str__(), "[Square] (3) 0/0 - 3")
        self.assertEqual(sqr2.__str__(), "[Square] (4) 5/6 - 4")

    def test_area(self):
        """
        Tests square area.
        """
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

    def test_save_to_file(self):
        """
        Tests save to file.
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_load_file(self):
        """
        Tests save load file.
        """
        r1 = Square(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Square.save_to_file([r1, r2])
        load_file = Square.load_from_file()
        self.assertTrue(isinstance(load_file, list))

    def test_to_dict(self):
        """
        Tests dict.
        """
        dict1 = self.sqr1.to_dictionary()
        self.assertEqual({"id": 1, "size": 2, "x": 4, "y": 0}, dict1)
        self.assertTrue(isinstance(dict1, dict))

    def test_inheritance(self):
        """
        Tests if Square inherits Base.
        """
        self.assertTrue(issubclass(Square, Base))


if __name__ == '__main__':
    unittest.main()
