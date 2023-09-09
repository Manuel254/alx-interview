#!/usr/bin/python3
"""This module contains the solution to prime game"""


def primeNums(n):
    """Returns all prime numbers in a range of numbers"""
    primes = [2]
    if n == 1:
        return []

    for num in range(3, n + 1):
        if num % 2 != 0:
            primes.append(num)
    return primes


def winner(my_winners):
    """Returns the winner of the game"""
    return max(set(my_winners), key=my_winners.count)


def isWinner(x, nums):
    """Return winner of Prime Game"""
    players = ["Maria", "Ben"]

    for _ in range(x):
        winners = []
        primes = []

        for num in nums:
            primes = primeNums(num)
            my_nums = [i for i in range(1, num + 1)]
            player = players[0]
            for prime in primes:
                if len(my_nums) == 1:
                    break
                for j in my_nums:
                    if prime == j or j % prime == 0:
                        my_nums.remove(j)
            players[0] = players[1]
            players[1] = player
            winners.append(players[0])

        return winner(winners)
