#!/usr/bin/python3
"""Defines a Base class."""


class Base:
    """
    Represent a Base class instance.

    Attributes:
        __nb_objects (int): The number of Base instances

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The id of the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
