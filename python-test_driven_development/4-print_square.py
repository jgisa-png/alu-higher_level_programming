#!/usr/bin/python3
"""
Module providing a function to print a square using '#' characters.

This module validates the size parameter to ensure it is a non-negative
integer before rendering the square.
"""


def print_square(size):
    """Prints a square with the character # of given integer size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
