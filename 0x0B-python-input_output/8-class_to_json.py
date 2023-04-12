#!/usr/bin/python3
"""
Defines a function that  returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
         Returns the dictionary description with simple data structure
         (list, dictionary, string, integer and boolean)
         for JSON serialization of an object

        Args:
            obj (obj): The object to return the description of

        Return: (dict) A dictionary containing details of the object
    """
    if not obj:
        return None

    return obj.__dict__
