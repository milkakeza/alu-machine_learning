#!/usr/bin/env python3
"""
Function that performs elementwise operations
"""


def np_elementwise(mat1, mat2):
    """Returns a tuple consisting of elementwise operations
    """
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return (add, sub, mul, div)
