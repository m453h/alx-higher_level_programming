#!/usr/bin/python3
"""Defines a Base class."""
import json


class Base:
    """
    Represent a Base class instance.

    Attributes:
        __nb_objects (int): The number of Base instances.

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): The list of dictionaries.

        Return:
            (string): JSON representation of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): The list of instances who inherits from Base.

        Return:
            (string): JSON representation of list_dictionaries.
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

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string.

        Args:
            json_string (str): String representing a list of dictionaries.

        Returns:
            (list): The list represented by json_string.
        """
        if json_string is None or json_string == "[]" or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of a class with all attributes set.

        Args:
            **dictionary (dict): Dictionary with attributes to initialize.

        Returns:
            (obj): The instance of a Rectangle or Square
                   with attributes in **dictionary.
        """
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)

            dummy.update(**dictionary)
            return dummy
