#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8
import json
import os

"""
Test Class
"""


class TestRectangleClass(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """
        setup class method
        """
        Base._Base__nb_objects = 0
        cls.rect1 = Rectangle(2, 4)
        cls.rect2 = Rectangle(2, 4, 6)
        cls.rect3 = Rectangle(2, 4, 6, 8)
        cls.rect4 = Rectangle(2, 4, 6, 8, 10)

    @classmethod
    def tearDownClass(self):
        """
        pass
        """

    def test_pep8(self):
        """
        Test that the code conforms to PEP8.
        """
        style = pep8.StyleGuide(quiet=True, exclude=["models/Square.json"])
        result = style.check_files(
            ['models/base.py', 'models/rectangle.py', 'models/square.py'])
        self.assertEqual(result.total_errors, 0, "Pep8 Error in file")

    def test_class(self):
        """
        Tests if Rectangle is a class.
        """
        self.assertTrue(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test_id_4(self):
        """
        Tests id.
        """
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)
        b4 = Base(69)
        b5 = Base(4)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 69)
        self.assertEqual(b5.id, 4)

    def test_id(self):
        """
        Tests id.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 4)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_to_dict(self):
        """
        Tests dict.
        """
        dict1 = self.rect1.to_dictionary()
        self.assertEqual(
            {"x": 0, "y": 0, "id": 1, "height": 4, "width": 2}, dict1)

    def test_area(self):
        """
        Tests area.
        """
        r1 = Rectangle(10, 10, 10, 10, 42)
        self.assertEqual(str(r1), "[Rectangle] (42) 10/10 - 10/10")

    def test_update(self):
        """
        Tests the update.
        """
        rect1 = {"id": 42, "width": 1, "height": 2, "x": 3, "y": 4}
        rect2 = {"id": 23, "width": 4, "height": 3, "x": 5, "y": 12}
        rdct_create1 = Rectangle.create(**rect1)
        rdct_create2 = Rectangle.create(**rect2)
        self.assertEqual("[Rectangle] (42) 3/4 - 1/2", str(rdct_create1))
        self.assertEqual("[Rectangle] (23) 5/12 - 4/3", str(rdct_create2))
        self.assertTrue(isinstance(rect1, dict))
        self.assertTrue(isinstance(rect2, dict))

    def test_save_to_file(self):
        """
        Tests save to file.
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_load_file(self):
        """
        Tests save load file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        load_file = Rectangle.load_from_file()
        self.assertTrue(isinstance(load_file, list))

    def test_args(self):
        """
        Tests args.
        """
        with self.assertRaises(TypeError):
            rect1 = Rectangle()
            self.rect1.area(1)

    def test_inheritance(self):
        """
        Tests if Rectangle inherits Base.
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_width_string(self):
        """
        Test string
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_save_to_file_empty_list(self):
        """
        Test save_to_file method with an empty list.
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_rectangle_list(self):
        """
        Test save_to_file method with a list of Rectangle objects.
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            data = json.load(f)
            self.assertTrue(isinstance(data, list))
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]['width'], 1)
            self.assertEqual(data[0]['height'], 2)
            self.assertEqual(data[1]['width'], 3)
            self.assertEqual(data[1]['height'], 4)

    def test_load_from_file_nonexistent_file(self):
        """
        Test load_from_file method with a nonexistent file.
        """
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        data = Rectangle.load_from_file()
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 0)

    def test_load_from_file_rectangle_file(self):
        """
        Test load_from_file method with a file containing Rectangle data.
        """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])

        data = Rectangle.load_from_file()
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0].width, 1)
        self.assertEqual(data[0].height, 2)
        self.assertEqual(data[1].width, 3)
        self.assertEqual(data[1].height, 4)

    def test_save_to_file_rectangle_list(self):
        """
        Test save_to_file method with a list of Rectangle objects.
        """
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 4)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as f:
            data = json.load(f)
            self.assertTrue(isinstance(data, list))
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]['id'], rect1.id)
            self.assertEqual(data[0]['width'], rect1.width)
            self.assertEqual(data[0]['height'], rect1.height)
            self.assertEqual(data[0]['x'], rect1.x)
            self.assertEqual(data[0]['y'], rect1.y)
            self.assertEqual(data[1]['id'], rect2.id)
            self.assertEqual(data[1]['width'], rect2.width)
            self.assertEqual(data[1]['height'], rect2.height)
            self.assertEqual(data[1]['x'], rect2.x)
            self.assertEqual(data[1]['y'], rect2.y)


if __name__ == '__main__':
    unittest.main()
