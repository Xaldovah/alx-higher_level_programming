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
    if isinstance(m_a, list) is False:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list) is False:
        raise TypeError("m_b must be a list")
    if not m_a:
        raise ValueError("m_a cannot be empty")
    if not m_b:
        raise ValueError("m_b cannot be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    if not all(isinstance(i, float) or isinstance(i, int)
               for elem in m_a for i in elem):
        raise ValueError("m_a should contain only integers or floats")
    if not all(isinstance(i, float) or isinstance(i, int)
               for elem in m_b for i in elem):
        raise ValueError("m_b should contain only integers or floats")
    if not all(isinstance(item, list) for item in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(item, list) for item in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")

    return [[
        sum(a * b for a, b in zip(a_row, b_col))
        for b_col in zip(*m_b)]
            for a_row in m_a]
