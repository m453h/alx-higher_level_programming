#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []
    row_num = 0
    for row in matrix:
        square_matrix.append([])
        for elem in row:
            square_matrix[row_num].append(elem ** 2)
        row_num = row_num + 1
    return square_matrix
