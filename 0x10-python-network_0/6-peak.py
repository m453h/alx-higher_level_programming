#!/usr/bin/python3
"""Defines a function that returns peak in a list of integers"""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        middle = (low + high) // 2

        if list_of_integers[middle] < list_of_integers[middle + 1]:
            low = middle + 1
        else:
            high = middle

    return list_of_integers[low]
