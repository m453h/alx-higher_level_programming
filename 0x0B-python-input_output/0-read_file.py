#!/usr/bin/python3
""" Defines a function that reads a text file and prints it to stdout """


def read_file(filename=""):
    """
        Reads a text file (UTF8) and prints it to stdout

        Args:
            filename (str): The name of the file to read
        Return: (None)
    """
    with open(filename, "r", encoding="utf-8") as input_file:
        print(input_file.read(), end="")
