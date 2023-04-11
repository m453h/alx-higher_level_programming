#!/usr/bin/python3
"""
    Defines a function to check if object is instance of,
    or if the object is an instance of a class that inherited from,
    a specified class

"""


def is_kind_of_class(obj, a_class):
    """
        Checks if an object is instance of,
        or if the object is an instance of a class that inherited from,
        a specified class

        Args:
            obj (obj): The object to check for instance type
            a_class (type): The class to match the type of obj to

        Returns: (bool) True if obj is f an object is instance of,
                        or if obj is an instance of a class inherited from,
                        a specified class of a_class
                        Else, False.

    """
    return isinstance(obj, a_class)
