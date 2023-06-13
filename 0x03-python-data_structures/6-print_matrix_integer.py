#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elements in matrix:
            a = 1
            length_of_elements = len(elements)

            for elems in elements:
                if a == length_of_elements:
                    print('{:d}'.format(elems), end="")
                else:
                    print('{:d}'.format(elems), end=" ")
                a += 1

            print()
