#!/usr/bin/python3

"""Defines a function that multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list): first matrix made of list of lists of integers/floats
        m_b (list): second matrix made of list of lists of integers/floats

    Raises:
        TypeError:  - When m_a or m_b is not a list of lists of ints/floats
                    - When m_a or m_b is empty
                    - When m_a or m_b have different-sized rows.

        ValueError: - When m_a or m_b is empty
                    - When m_a and m_b cannot be multiplied.
    """
    errors = {
        "m_a_not_list": "m_a must be a list",
        "m_b_not_list": "m_b must be a list",
        "m_a_empty": "m_a can't be empty",
        "m_b_empty": "m_b can't be empty",
        "m_a_not_llist": "m_a must be a list of lists",
        "m_b_not_llist": "m_b must be a list of lists",
        "m_a_non_number": "m_a should contain only integers or floats",
        "m_b_non_number": "m_b should contain only integers or floats",
        "m_a_row_size": "each row of m_a must should be of the same size",
        "m_b_row_size": "each row of m_b must should be of the same size",
        "cant_multiply": "m_a and m_b can't be multiplied"
        }

    if not isinstance(m_a, list):
        raise TypeError(errors["m_a_not_list"])

    if not isinstance(m_b, list):
        raise TypeError(errors["m_b_not_list"])

    if m_a == [] or m_a == [[]]:
        raise ValueError(errors["m_a_empty"])

    if m_b == [] or m_b == [[]]:
        raise ValueError(errors["m_b_empty"])

    for row in m_a:
        if not isinstance(row, list) or row is None:
            raise TypeError(errors["m_a_not_llist"])

        if len(m_a[0]) != len(row):
            raise TypeError(errors["m_a_row_size"])

        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError(errors["m_a_non_number"])

    for row in m_b:
        if not isinstance(row, list) or row is None:
            raise TypeError(errors["m_b_not_llist"])

        if len(m_b[0]) != len(row):
            raise TypeError(errors["m_b_row_size"])

        for n in row:
            if not isinstance(n, int) and not isinstance(n, float):
                raise TypeError(errors["m_b_non_number"])

    if len(m_a[0]) != len(m_b):
        raise ValueError(errors["cant_multiply"])

    flipped_mb = []
    for i in range(0, len(m_b[0])):
        row = []
        for j in range(0, len(m_b)):
            row.append(m_b[j][i])
        flipped_mb.append(row)

    result = []
    for row in m_a:
        result_row = []
        for col in flipped_mb:
            product = 0
            for i in range(len(flipped_mb[0])):
                product = product + (row[i] * col[i])
            result_row.append(product)
        result.append(result_row)

    return result
