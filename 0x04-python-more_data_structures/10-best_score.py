#!/usr/bin/python3

def best_score(a_dictionary):
    max_int = None
    key = ""
    if a_dictionary is None or len(a_dictionary) == 0:
        return max_int

    for k in a_dictionary:
        if max_int is None:
            key = k
            max_int = a_dictionary[k]

        if a_dictionary[k] > max_int:
            key = k
            max_int = a_dictionary[k]

    return key
