#!/usr/bin/python3
"""This module contains the solution to UTF-8 validation
problem
"""


def validUTF8(data):
    """Determines if a given data set represents
    a valid UTF-8 encoding"""
    counter = 0

    for number in data:
        bin_num = bin(number)[2:]
        if len(bin_num) > 8:
            number <<= bin_num - 8
        if counter == 0:
            if number >> 5 == 0b110:
                counter = 1
            elif number >> 4 == 0b1110:
                counter = 2
            elif number >> 3 == 0b11110:
                counter = 3
            elif not number >> 7 == 0b0:
                return False
        else:
            if not number >> 6 == 0b10:
                return False
            counter -= 1
    return counter == 0
