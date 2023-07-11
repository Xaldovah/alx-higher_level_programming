#!/usr/bin/python3
"""append_after function module"""


def append_after(filename="", search_string="", new_string=""):
    """append_after function"""
    with open(filename, "r", encoding="utf-8") as f:
        content = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in content:
            f.write(line)
            if search_string in line:
                f.write(new_string)
