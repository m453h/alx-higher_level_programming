#!/usr/bin/python3
""" Defines a function that returns a Python object represented a JSON string """
import json


def from_json_string(my_str):
    """
        Returns an object (Python data structure) represented by a JSON string

        Args:
            my_str (string): The JSON string to convert to an object

        Return: (object) Python object represented by my_str
    """
    return json.loads(my_str)
