#!/usr/bin/python3
"""This module contains the solution for the log parsing problem"""
from sys import stdin


def print_status_codes(code, file_size):
    """Prints the status code with its count.
    Format:
        <status>: <count>
    """
    for key, val in sorted(code.items()):
        print("{}: {}".format(key, val))


code = {}
file_size = 0
vals_total = 0

try:
    for line in stdin:
        line = line.split()
        file_size += int(line[-1])
        status = line[-2]
        vals = list(code.values())
        vals_total = sum(vals)

        print("File size: {}".format(file_size))

        if status not in code:
            code[status] = 1  
        else:
            code[status] += 1

        vals_total += 1
        print_status_codes(code, file_size)

        if vals_total % 10 == 0:
            continue
except KeyboardInterrupt:
    print_status_codes(code, file_size)