#!/usr/bin/python3

"""Defines a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix with a number

    Args:
        matrix (list): list of lists of integers/floats
        div (number): integer or float

    Raises:
        TypeError: if matrix is not list of lists of integers/floats
                   or matrix does not contain rows with the same size
                   or div is not an integer/float

        ZeroDivisionError: if div is equal to 0
    """
    errors = {
            "01": "matrix must be a matrix (list of lists) of integers/floats",
            "02": "Each row of the matrix must have the same size",
            "03": "div must be a number",
            "04": "division by zero"
            }

    if not isinstance(matrix, list) or matrix == [] or matrix is None:
        raise TypeError(errors["01"])
    for row in matrix:
        if not isinstance(row, list) or row is None:
            raise TypeError(errors["01"])

        if len(matrix[0]) != len(row):
            raise TypeError(errors["02"])

        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError(errors["01"])

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(errors["03"])

    if div == 0:
        raise ZeroDivisionError(errors["04"])

    div_matrix = []
    row_num = 0

    for row in matrix:
        div_matrix.append([])
        for n in row:
            div_matrix[row_num].append(round(n / div, 2))
        row_num = row_num + 1

    return div_matrix
