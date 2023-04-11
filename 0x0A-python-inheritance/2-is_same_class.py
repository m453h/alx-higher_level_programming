#!/usr/bin/python3
""" Defines a function to check if object is an exact instance of a class"""


def is_same_class(obj, a_class):
    """
        Checks if an object is exactly an instance of a specified class

        Args:
            obj (obj): The object to check for instance type
            a_class (type): The class to match the type of obj to

        Returns: (bool) True if obj is exact instance of a_class Else, False.

    """
    return type(obj) == a_class
