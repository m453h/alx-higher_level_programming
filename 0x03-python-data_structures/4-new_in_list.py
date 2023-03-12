#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return None
    my_list_len = len(my_list)

    if idx >= my_list_len:
        return None

    new_list = my_list.copy()
    new_list[idx] = element

    return new_list
