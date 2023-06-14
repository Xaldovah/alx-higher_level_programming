#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()

    for i, j in new_dictionary.items():
        new_dictionary[i] = j * 2

    return new_dictionary
