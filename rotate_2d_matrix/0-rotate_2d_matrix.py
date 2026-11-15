#!/usr/bin/python3
"""
Function that rotates a 2d matrix
"""


def rotate_2d_matrix(matrix):
    new_matrix = []
    for item in matrix[0]:
        new_matrix.append([])
    i = 0
    for row in matrix:
        for i, item in enumerate(row):
            new_matrix[i].insert(0, item)
    matrix[:] = new_matrix
