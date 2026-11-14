#!/usr/bin/python3
"""Define a square with a size and a position."""


class Square:
    """Represent a square that can be printed at an offset."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the side length and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the horizontal and vertical offsets."""
        return self.__position

    @position.setter
    def position(self, value):
        """Validate and update the position."""
        valid_pair = isinstance(value, tuple) and len(value) == 2
        if not valid_pair or not all(
                isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square at its position."""
        if self.__size == 0:
            print()
            return
        x, y = self.__position
        for _ in range(y):
            print()
        for _ in range(self.__size):
            print(" " * x + "#" * self.__size)
