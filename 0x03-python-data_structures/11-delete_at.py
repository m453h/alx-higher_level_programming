#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_list_len = len(my_list)

    if idx < 0:
        return my_list

    if idx >= my_list_len:
        return my_list

    new_list = my_list.copy()
    my_list.clear()

    i = 0
    for n in new_list:
        if i != idx:
            my_list.append(n)

        i = i + 1

    return my_list
