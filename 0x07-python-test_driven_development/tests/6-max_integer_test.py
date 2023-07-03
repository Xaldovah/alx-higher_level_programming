#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class to test the max integer
    """

    def test_max_integer(self):
        """
        Test the max integer in a list when the integers
        are positive or negative numbers
        """
        self.assertIsNone(max_integer([]))
        self.assertAlmostEqual(max_integer([1, 3, 5, 7, 9]), 9)
        self.assertAlmostEqual(max_integer([-7, -5, -3, -1, 0]), 0)
        self.assertAlmostEqual(max_integer([-54, -70, -230, -154]), -54)
        self.assertAlmostEqual(max_integer([4.0, 3.3, 5.9, 1.8, 0.7]), 5.9)
        self.assertAlmostEqual(max_integer([2.6]), 2.6)

    def test_error_types(self):
        """
        Test the max integer which will raise error messages
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["House", 95, 73, -43, "Key"])
