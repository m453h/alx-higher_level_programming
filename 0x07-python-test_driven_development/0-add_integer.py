#!/usr/bin/python3

"""Defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """ Adds two integers

    Args:
        a (int): The first number to add
        b (int): The second number to add

    Raises:
        TypeError:  if a or b are not integers or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a + b)
