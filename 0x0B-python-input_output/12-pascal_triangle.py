#!/usr/bin/python3
"""
 Defines a function that returns a list of lists
 of integers representing the Pascal’s triangle of n:

"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers
    representing the Pascal’s triangle of n.

    Args:
        n (int): Number of rows on the triangle to generate.

    Return:
        (list): List of lists of integers representing Pascal's triangle of n.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        factorial = 1
        for j in range(i + 1):
            if j > 0:
                factorial = int(factorial * (i - j + 1) / j)
            row.append(factorial)

        triangle.append(row)

    return triangle
