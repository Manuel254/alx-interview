#!/usr/bin/python3
"""This module contains solution to island perimeter problem"""

def island_perimeter(grid):
    """"Island perimeter solution"""
    visited = set()

    def dfs(i, j):
        if i >= len(grid) or j >= len(grid[0]) or \
            i < 0 or j < 0 or not grid[i][j]:
            return 1
        if (i, j) in visited:
            return 0
        
        visited.add((i, j))
        perimeter = dfs(i, j + 1)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i - 1, j)
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j)
    