#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    if len(matrix) > 0:
        for i in matrix[:]:
            new_matrix.append(list(map(lambda x: x ** 2, i)))

    return new_matrix
