#!/usr/bin/python3
"""This module contains solution to make change"""


def makeChange(coins, total):
    """Calculate fewest number of coins to meet a given
    amount of total
    Return:
        count of coins
        else:
            0 if total is 0
            -1 if total cannot be met by any number of coins
    """
    count = 0
    if total <= 0:
        return 0

    while len(coins) > 0 and total >= 0:
        max_num = max(coins)
        diff = total - max_num

        if diff >= 0:
            count += 1
            total = diff
        else:
            coins.remove(max_num)

    if count and total == 0:
        return count
    else:
        return -1
