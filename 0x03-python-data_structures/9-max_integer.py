#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_int = my_list[0]
    for n in my_list:
        if max_int < n:
            max_int = n

    return max_int
