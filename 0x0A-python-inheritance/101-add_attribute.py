#!/usr/bin/python3
""" Defines a function returning list of attributes and methods of an object"""


def add_attribute(obj, attribute, value):
    """
        Adds a new attribute to an object if possible.

        Args:
            obj (obj): The object to add new attribute to.
            attribute (str): The name of the attribute to add.
            value (any): The value of the newly defined attribute.

        Raises:
                TypeError: If obj can't have the new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
        
    setattr(obj, attr, value)
