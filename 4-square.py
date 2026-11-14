#!/usr/bin/python3
"""Define a square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the square."""
        self.size = size

    @property
    def size(self):
        """Return the side length."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and update the side length."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
