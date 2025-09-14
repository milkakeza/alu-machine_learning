#!/usr/bin/env python3
"""
This module contains the function matrix_shape which calculates
the shape of matrix and returns it as a list of integers.
"""


def matrix_shape(matrix):
    # Function for calculating shape of matrix
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
