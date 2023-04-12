#!/usr/bin/python3
""" Defines a function that returns JSON representation of an object """
import json


def to_json_string(my_obj):
    """
        Returns the JSON representation of an object (string)

        Args:
            my_obj (obj): The object to return JSON representation

        Return: (string) JSON representation of my_obj
    """
    return json.dumps(my_obj)
