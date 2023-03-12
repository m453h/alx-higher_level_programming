#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    start = len(my_list) - 1
    for x in range(start, -1, -1):
        print("{:d}".format(my_list[x]))
