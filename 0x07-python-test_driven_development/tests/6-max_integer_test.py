#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Represents unit test class for max_integer module """
    
    def test_ascending_ordered_list(self):
        """Test for ascending ordered list of integers input."""
        x = [1, 2, 3, 4]
        self.assertEqual(max_integer(x), 4)

    def test_descending_ordered_list(self):
        """Test for descending ordered list of integers input."""
        x = [4, 3, 2, 1]
        self.assertEqual(max_integer(x), 4)

    def test_unordered_list(self):
        """Test for unordered list of integers input."""
        x = [3, 4, 1, 2]
        self.assertEqual(max_integer(x), 4)

    def test_list_with_one_element(self):
        """Test a list with one element input."""
        one_element = [3]
        self.assertEqual(max_integer(one_element), 3)

    def test_empty_list(self):
        """Test an empty list input."""
        self.assertEqual(max_integer([]), None)

    def test_list_of_floats(self):
        """Test a list of floats input."""
        x = [3.14, 3.15, 3.16, 4.2, 8.8]
        self.assertEqual(max_integer(x), 8.8)


if __name__ == '__main__':
    unittest.main()