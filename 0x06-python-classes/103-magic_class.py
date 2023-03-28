#!/usr/bin/python3
"""Define a MagicClass matching exactly given bytecode in Task 10."""


import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a new instance of the MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass instance.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass instance."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass instance."""
        return (2 * math.pi * self.__radius)
