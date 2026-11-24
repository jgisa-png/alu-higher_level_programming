#!/usr/bin/python3
"""
Module providing a function to multiply two matrices using NumPy.

This module uses numpy.matmul to perform matrix multiplication on two
validated input matrices.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b using NumPy's matmul."""
    return np.matmul(m_a, m_b)
