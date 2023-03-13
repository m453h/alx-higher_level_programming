#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    my_list_len = len(my_list)

    if idx >= my_list_len:
        return None

    return my_list[idx]
