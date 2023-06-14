#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for i, j in a_dictionary.items():
        if j == value:
            keys.append(i)

    for i in keys:
        del a_dictionary[i]

    return a_dictionary
