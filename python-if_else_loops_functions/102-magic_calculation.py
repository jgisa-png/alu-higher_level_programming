#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Perform the comparisons and calculation from the bytecode."""
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
