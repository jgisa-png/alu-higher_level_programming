#!/usr/bin/python3
def safe_print_integer(value):
    try:
        text = "{:d}".format(value)
    except (TypeError, ValueError):
        return False
    print(text)
    return True
