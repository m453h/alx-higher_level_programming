#!/usr/bin/python3

"""Defines MyList class."""


class MyList(list):
    """Represent MyList instance."""

    def print_sorted(self):
        """
            Prints MyList in ascending sorted order
            Return: (list) - sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
