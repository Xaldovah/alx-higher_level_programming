#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except TypeError:
        pass

    print()  # Print a new line after printing the integers
    return count

