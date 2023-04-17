#!/usr/bin/python3
"""Defines unittest classes for Rectangle class in models.rectangle"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle__init__(unittest.TestCase):
    """Unittests for the Rectangle class __init__ method"""

    def test_init_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_init_multiple_squares_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
            RectangleRectangle()
            Rectangle()

    def test_init_with_none_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_is_instance_of_base(self):
        r1 = Rectangle(5, 10)
        self.assertIsInstance(r1, Base)

    def test_is_instance_of_rectangle(self):
        r1 = Rectangle(10, 15)
        self.assertIsInstance(r1, Rectangle)

    def test_init_with_one_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(5)
            self.assertIsInstance(r1, Base)

    def test_init_with_two_args(self):
        r1 = Rectangle(8, 6)
        r2 = Rectangle(2, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_init_with_three_args(self):
        r1 = Rectangle(2, 4, 6)
        r2 = Rectangle(3, 6, 9)
        r3 = Rectangle(4, 8, 12)
        self.assertEqual(r2.id, r3.id - 1)

    def test_init_with_five_args(self):
        r1 = Rectangle(10, 2, 2, 7, 8)
        self.assertEqual(8, r1.id)

    def test_init_with_more_than_allowed_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangle_area(unittest.TestCase):
    """Unittests for the Rectangle class area method"""

    def test_area_small_int(self):
        self.assertEqual(9, Rectangle(3, 3, 0, 1, 9).area())

    def test_area_large_int(self):
        length = 489498498498498498498498498
        width = 489498498498498498498498498

        s = Rectangle(length, width, 0, 1, 7)
        r = 239608780032284536789041293057769517265012760508256004
        self.assertEqual(r, s.area())

    def test_area_float(self):
        with self.assertRaises(TypeError):
            s = Square(3.5, 0, 0, 1)
            r = 12.25
            self.assertEqual(r, s.area())


if __name__ == "__main__":
    unittest.main()
