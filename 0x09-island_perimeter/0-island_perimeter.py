#!/usr/bin/python3
"""
Problem Solution
"""


def checkCell(grid, row, column):
    """
    Take a single cell check it's upper
    lower left and right to count the edges
    """
    sides = 0
    row_length = len(grid)
    column_length = len(grid[0])
    if row - 1 < 0 or grid[row - 1][column] == 0:
        sides += 1
    if row + 1 >= row_length or grid[row + 1][column] == 0:
        sides += 1
    if column - 1 < 0 or grid[row][column - 1] == 0:
        sides += 1
    if column + 1 >= column_length or grid[row][column + 1] == 0:
        sides += 1
    return sides


def island_perimeter(grid):
    """
    iterate over the cells and check each
    """
    perimeter = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                perimeter += checkCell(grid, row, column)
    return perimeter
