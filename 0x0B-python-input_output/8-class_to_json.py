#!/usr/bin/python3
"""
Defines a function that  returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""
import json


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

    obj_dictionary = {}
    attributes = dir(obj)

    for attribute in attributes:

        if callable(getattr(obj, attribute)) or attribute.startswith("__"):
            continue
            
        attribute_value = getattr(obj, attribute)
       
        if isinstance(attribute_value, (list, dict, str, int, bool)):
            obj_dictionary[attribute] = attribute_value

    return obj_dictionary