#!/usr/bin/python3

"""Defines a function that prints a full name"""


def say_my_name(first_name, last_name=""):
    """ Prints first name and last name

    Args:
        first_name (string): First name to print
        last_name (string): Last name to print

    Raises:
        TypeError: If First name or Last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
