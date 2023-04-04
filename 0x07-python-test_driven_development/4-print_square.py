#!/usr/bin/python3

"""Defines a function that prints a square with character #"""


def print_square(size):
    """ Prints a square with a character #

    Args:
        size (int): Length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        print("#" * size)
