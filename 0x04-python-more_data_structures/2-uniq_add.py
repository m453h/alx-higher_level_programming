#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum = 0
    for n in my_set:
        sum = sum + n
    return sum
