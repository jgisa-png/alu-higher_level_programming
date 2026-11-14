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
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square positioned for printing."""
        if self.size == 0:
            return ""
        x, y = self.position
        row = " " * x + "#" * self.size
        return "\n" * y + "\n".join([row] * self.size)

    def my_print(self):
        """Print the square at its position."""
        print(self)
