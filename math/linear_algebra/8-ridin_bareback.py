#!/usr/bin/env python3
"""
Function performs matrix multiplication between two 2D matrices.
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication between two 2D matrices.
    """
    if len(mat1[0]) != len(mat2):
        return None
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum_prod = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
            row.append(sum_prod)
        result.append(row)
    return result
