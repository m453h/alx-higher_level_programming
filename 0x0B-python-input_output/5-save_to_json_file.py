#!/usr/bin/python3
""" Defines a function that writes an Object to a text file in JSON format """
import json


def save_to_json_file(my_obj, filename):
    """
        Writes an Object to a text file, using a JSON representation

        Args:
            filename (str): The name of the file to write to
            my_obj (obj): The object to write to the file

        Return: (int) number of characters written to the file
    """
    with open(filename, "w", encoding="utf-8") as output_file:
        output_file.write(json.dumps(my_obj))
