#!/usr/bin/python3
"""Defines a function that returns peak in a list of integers"""


def find_peak(list_of_integers):
    """Returns peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        middle = (low + high) // 2

        if list_of_integers[middle] < list_of_integers[middle + 1]:
            low = middle + 1
        else:
            high = middle

    return list_of_integers[low]
