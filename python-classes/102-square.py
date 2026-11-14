#!/usr/bin/python3
"""Define a square with a size property."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the side length."""
        self.size = size

    @property
    def size(self):
        """Return the side length."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and update the side length."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare the areas for equality."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __lt__(self, other):
        """Check whether this square has a smaller area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Check whether this area is smaller or equal."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check whether this square has a larger area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Check whether this area is larger or equal."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
