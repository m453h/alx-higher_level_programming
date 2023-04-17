#!/usr/bin/python3
"""Defines unittest classes for Square class in models.square"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare__init__(unittest.TestCase):
    """Unittests for the Square class __init__ method"""

    def test_init_with_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_init_multiple_squares_with_no_args(self):
        with self.assertRaises(TypeError):
            Square()
            Square()
            Square()
    
    def test_init_with_none_arg(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_is_instance_of_base(self):
        s1 = Square(5)
        self.assertIsInstance(s1, Base)

    def test_is_instance_of_rectangle(self):
        s1 = Square(5)
        self.assertIsInstance(s1, Square)

    def test_init_with_one_arg(self):
        s1 = Square(5)
        s2 = Square(6)
        self.assertEqual(s1.id, s2.id - 1)

    def test_init_with_two_args(self):
        s1 = Square(8, 6)
        s2 = Square(2, 4)
        self.assertEqual(s1.id, s2.id - 1)

    def test_init_with_three_args(self):
        s1 = Square(2, 4, 6)
        s2 = Square(3, 6, 9)
        s3 = Square(4, 8, 12)
        self.assertEqual(s2.id, s3.id - 1)

    def test_init_with_four_args(self):
        s1 = Square(10, 2, 2, 7)
        self.assertEqual(7, s1.id)

    def test_init_with_more_than_allowed_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)

if __name__ == "__main__":
    unittest.main()
