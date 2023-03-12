#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        row_length = len(row)
        element_counter = 1
        for element in row:
            if element_counter == row_length:
                sep = ""
            else:
                sep = " "

            print("{:d}".format(element), end=sep)
            element_counter = element_counter + 1
        print("")
