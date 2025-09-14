#!/usr/bin/env python3
"""
Function concatenates two NumPy arrays along a specified axis.
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two NumPy arrays along a specified axis.
    """
    return np.concatenate((np.array(mat1), np.array(mat2)), axis=axis)
