#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_a_dictionary = {}
    for k in a_dictionary:
        new_a_dictionary[k] = a_dictionary[k] * 2
    return new_a_dictionary
