#!/usr/bin/python3
""" Defines a function that creates an Object from a JSON file """
import json


def load_from_json_file(filename):
    """
        Creates an Object from a JSON file

        Args:
            filename (str): The name of the file to write to

        Return: (obj) Object created from the JSON file
    """
    with open(filename, "r", encoding="utf-8") as input_file:
        return json.loads(input_file.read())
