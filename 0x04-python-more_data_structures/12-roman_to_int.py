#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    num_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and num_map[roman_string[i]] < num_map[roman_string[i + 1]]:
            result -= num_map[roman_string[i]]
        else:
            result += num_map[roman_string[i]]
    return result
