#!/usr/bin/python3
import sys


def print_stats():
    print('File size: {:d}'.format(file_size))

    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

it = 0
file_size = 0

try:
    for line in sys.stdin:
        if it != 0 and it % 10 == 0:
            print_stats()

        pieces = line.split()

        try:
            status = int(pieces[-2])

            if str(status) in status_codes.keys():
                status_codes[str(status)] += 1
        except ValueError:
            pass

        try:
            file_size += int(pieces[-1])
        except ValueError:
            pass

        it += 1

    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
