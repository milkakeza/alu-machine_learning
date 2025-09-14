#!/usr/bin/env python3
"""
    Function adds two 2D matrices element-wise, and 
    returns the list of lists or None: Element-wise sum if shapes match, else None.
    """


def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise, and 
    returns the list of lists or None: Element-wise sum if shapes match, else None.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(mat1, mat2)]
