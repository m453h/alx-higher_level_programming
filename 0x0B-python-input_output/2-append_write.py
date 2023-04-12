#!/usr/bin/python3
""" Defines a function that appends a string to the end of a text file """


def append_write(filename="", text=""):
    """
        Writes a string by appending to the end of a text file (UTF8)

        Args:
            filename (str): The name of the file to write to
            text (str): The string to append to the file

        Return: (int) number of characters appended to the file
    """
    with open(filename, "a", encoding="utf-8") as output_file:
        return output_file.write(text)
