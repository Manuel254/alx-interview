#!/usr/bin/python3
"""This module contains the solution to 2d matrix rotation"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix in 90 degrees and
    edits it in-place
    """
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            t, b = l, r
            tl = matrix[t][l + i]
            matrix[t][l + i] = matrix[b - i][l]
            matrix[b - i][l] = matrix[b][r - i]
            matrix[b][r - i] = matrix[t + i][r]
            matrix[t + i][r] = tl
        l += 1
        r -= 1
