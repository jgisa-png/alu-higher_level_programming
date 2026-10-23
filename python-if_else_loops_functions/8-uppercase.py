#!/usr/bin/python3
def uppercase(str):
    """Print a string with ASCII lowercase letters converted to uppercase."""
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
