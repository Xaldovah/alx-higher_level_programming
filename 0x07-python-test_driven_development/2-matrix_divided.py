#!/usr/bin/python3

"""
Divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides a matrix
    """
    Error1 = "matrix must be a matrix (list of lists) of integers/floats"
    Error2 = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(Error1)
    for item in range(len(matrix)):
        if item != 0:
            result = item - 1
            if len(matrix[item]) != len(matrix[result]):
                raise TypeError(Error2)
    if isinstance(div, int) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in elem] for elem in matrix]
