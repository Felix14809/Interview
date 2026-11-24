#!/usr/bin/env python3
""""
Function that calculates the perimeter of an island in a grid
"""


def island_perimeter(grid) -> int:
    perimeter = 0
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == 1:
                perimeter += check_cell(grid, x, y)
    return perimeter


def check_cell(grid, row, col) -> int:
    perimeter = 4
    height = len(grid)
    width = len(grid[row])
    if row + 1 < height:
        if grid[row + 1][col] == 1:
            perimeter -= 1
    if row > 0:
        if grid[row - 1][col] == 1:
            perimeter -= 1
    if col + 1 < width:
        if grid[row][col + 1] == 1:
            perimeter -= 1
    if col > 0:
        if grid[row][col - 1] == 1:
            perimeter -= 1
    return perimeter
