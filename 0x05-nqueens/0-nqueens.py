#!/usr/bin/python3
"""N Queens problem"""
import sys


def solutions(row, column):
    solution = [[]]
    for queen in range(row):
        solution = place(queen, column, solution)
    return solution


def place(queen, column, prev_solution):
    pos = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                pos.append(array + [x])
    return pos


def is_safe(q, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():
    n = init()
    slns = solutions(n, n)
    for array in slns:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
