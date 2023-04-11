#!/usr/bin/python3
def lookup(obj):
    """
        Returns the list of available attributes and methods of an object

        Args:
            obj (obj): The object to print details
        Return: (list) list of attributes and methods
    """
    return dir(obj)
