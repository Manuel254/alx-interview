#!/usr/bin/python3
"""Module that implements minimum operations solution"""


def minOperations(n):
    """calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0
    
    operations = 0
    buffer = 0
    file = 1

    while file < n:
        if n % file == 0:
            buffer = file
            operations += 1
        file += buffer
        operations += 1
    return operations