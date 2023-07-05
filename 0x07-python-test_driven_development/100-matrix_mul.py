#!/usr/bin/python3
"""Matrix multiplication module"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices `m_a` and `m_b`.

    Args:
        m_a (list): The first matrix represented as a list of lists.
        m_b (list): The second matrix represented as a list of lists.

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        TypeError: If `m_a` or `m_b` is not a list,
        or if the elements of `m_a` or `m_b` are not lists.
        ValueError: If `m_a` or `m_b` is empty, or if the number of columns
        in `m_a` is not equal to the number of rows in `m_b`.
        TypeError: If the elements of `m_a` or `m_b` are not integers or floats
        TypeError: If the rows of `m_a` or `m_b` are not of the same size.

    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    return [[sum(a * b for a, b in zip(row_a, column_b))
             for column_b in zip(*m_b)] for row_a in m_a]
