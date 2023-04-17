#!/usr/bin/python3
"""Defines a Base class."""
import json


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

    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): The list of dictionaries

        Return:
            (string): JSON representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
