#!/usr/bin/python3
"""
    Defines a function that checks if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class

"""


def inherits_from(obj, a_class):
    """
        Checks if an object is instance of, a class that inherited from,
        a specified class

        Args:
            obj (obj): The object to check for inheritance
            a_class (type): The class type to compare with obj for inheritance

        Returns: (bool) True if obj is an instance of a class inherited from,
                        a specified class of a_class (directly or indirectly)
                        Else, False.

    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
