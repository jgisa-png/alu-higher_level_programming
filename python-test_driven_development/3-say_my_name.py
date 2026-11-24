#!/usr/bin/python3
"""
Module providing a function to print a formatted full name.

This module validates that first_name and last_name are strings before
printing them to standard output.
"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>' after type checking."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
