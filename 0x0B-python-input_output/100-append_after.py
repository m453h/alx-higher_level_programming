#!/usr/bin/python3
"""
Defines a function that inserts a line of text to a file,
after each line containing a specific string.

"""


def append_after(filename="", search_string="", new_string=""):
    """
        Inserts a line of text to a file, after each line
        containing a specific string.

        Args:
            filename (str): The name of the file to write to
            search_string (str): The string to search before insertion
            new_string (str): The string to append to the file

        Return: (nothing)
    """
    content = ""
    with open(filename, "r+", encoding="utf-8") as input_file:
        for line in input_file:
            content += line
            if search_string in line:
                content += new_string

    with open(filename, "w", encoding="utf-8") as output_file:
        output_file.write(content)
