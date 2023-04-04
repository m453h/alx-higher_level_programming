#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices using NumPy

    Args:
        m_a (list): The first matrix to multiply
        m_b (list): The second matrix to multiply

    Raises:
        ValueError:  If the last dimension of x1 is not
        the same size as the second-to-last dimension of x2.
        or If a scalar value is passed in
    """
    return np.matmul(m_a, m_b)
