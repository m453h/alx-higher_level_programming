#!/usr/bin/python3

"""Defines a function that prints 2 new lines after ., ?, and :"""


def text_indentation(text):
    """ Prints two new lines after ., ?, and : characters

    Args:
        text (string): input text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    is_start_of_line = True
    text = text.strip(" ")
    for c in text:
        if is_start_of_line and c == " ":
            continue

        print(c, end="")
        if c != "\n":
            is_start_of_line = False
        else:
            is_start_of_line = True

        if c in ".?:":
            is_start_of_line = True
            print("\n")
