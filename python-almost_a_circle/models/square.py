#!/usr/bin/python3
"""
Module defining the Square class inheriting from Rectangle.

This module implements a square shape where width and height are equal
and managed through the size property.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance using Rectangle's constructor."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets and validates both width and height to value."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes via positional or keyword args."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, val in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], val)
        else:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
