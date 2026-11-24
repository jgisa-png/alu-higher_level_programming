#!/usr/bin/python3
"""
Module providing a function to format text with double newlines.

This module splits text after '.', '?', and ':' characters while
stripping leading and trailing spaces on each line.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length and text[i] == " ":
        i += 1

    while i < length:
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1
