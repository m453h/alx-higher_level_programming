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
        for j in range(i + 1):
            row.append(int(factorial(i) / (factorial(j) * factorial(i - j))))

        triangle.append(row)

    return triangle


def factorial(n):
    """
    Calculates factorial of a number.

    Args:
        n (int): Number to calculate factorial.

    Returns:
        (int): Factorial of the given number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
