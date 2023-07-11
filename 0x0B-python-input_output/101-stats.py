#!/usr/bin/python3
"""print_stats function module"""

import sys


def print_stats(total_size, status_codes):
    """print_stats function"""
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {}

try:
    for i, line in enumerate(sys.stdin, 1):
        line = line.strip()
        data = line.split(" ")
        if len(data) >= 7:
            size = int(data[-1])
            code = data[-2]
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
            else:
                status_codes[code] = 1
        if i % 10 == 0:
            print_stats(total_size, status_codes)
except KeyboardInterrupt:
    print_stats(total_size, status_codes)
