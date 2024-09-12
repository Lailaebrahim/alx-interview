#!/usr/bin/python3
"""Rotate 2D Matrix in place """


def matrixTranspose(matrix):
    """Find Matrix Transpose"""
    for i in range(0, len(matrix[0]) - 1):
        for j in range(i+1, (len(matrix[0]))):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


def rotate_2d_matrix(matrix):
    """
    Rotate 2D Matrix in place

    Args:
        matrix :  a 2D Matrix
    """
    matrixTranspose(matrix)

    for i in range(len(matrix[0])):
        matrix[i] = list(reversed(matrix[i]))
