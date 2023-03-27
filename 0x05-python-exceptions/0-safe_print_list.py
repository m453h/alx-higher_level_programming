#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    print_count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            print_count = print_count + 1
        except IndexError:
            break
    print("")
    return print_count
