#!/usr/bin/env python3
"""
Performs element-wise operations on two numpy arrays (matrices).
"""
import numpy as np


def np_elementwise(mat1, mat2):
    """
    Performs element-wise operations on two numpy arrays (matrices).
    """
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
