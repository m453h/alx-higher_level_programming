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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): The list of instances who inherits from Base

        Return:
            (string): JSON representation of list_dictionaries
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__+".json"
        current_json_list = []

        for obj in list_objs:
            current_json_list.append(obj.to_dictionary())

        output = cls.to_json_string(current_json_list)

        with open(filename, 'w') as file:
            file.write(output)
