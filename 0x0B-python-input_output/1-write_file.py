#!/usr/bin/python3
""" Defines a function that writes a string to a text file """


def write_file(filename="", text=""):
    """
        Writes a string to a text file (UTF8)

        Args:
            filename (str): The name of the file to write to
            text (str): The string to write to the file

        Return: (int) number of characters written to the file
    """
    with open(filename, "w", encoding="utf-8") as output_file:
        return output_file.write(text)
