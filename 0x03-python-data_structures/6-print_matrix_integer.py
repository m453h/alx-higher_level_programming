#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new_str = ""

    for row in matrix:
        for element in row:
            print("{:d} ".format(element), end="")
        print("")
