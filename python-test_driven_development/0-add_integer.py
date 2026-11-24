#!/usr/bin/python3
"""
Module providing a function to add two integers.

This module defines add_integer which validates that inputs are integers
or floats before returning their integer sum.
"""


def add_integer(a, b=98):
    """Adds two integers or floats cast to integers and returns the sum."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
