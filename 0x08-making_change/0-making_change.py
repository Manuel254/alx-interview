#!/usr/bin/python3


def makeChange(coins, total):
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
