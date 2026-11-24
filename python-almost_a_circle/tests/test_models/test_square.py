#!/usr/bin/python3
"""Unit tests for the Square class in models/square.py."""
from io import StringIO
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class functionality and validation."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_valid_instantiation(self):
        """Test valid Square instantiation and size getter/setter."""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(3, 1, 2, 10)
        self.assertEqual(s2.id, 10)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 2)

    def test_size_validation(self):
        """Test TypeError and ValueError on Square size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3)

        s = Square(4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1

    def test_offset_validation(self):
        """Test validation of x and y offsets on Square."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "1")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 0, "1")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 0, -1)

    def test_str_area_display(self):
        """Test __str__, area, and display methods on Square."""
        s = Square(3, 1, 2, 7)
        self.assertEqual(str(s), "[Square] (7) 1/2 - 3")
        self.assertEqual(s.area(), 9)

        captured = StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n ###\n ###\n ###\n")

    def test_update(self):
        """Test update method with *args and **kwargs on Square."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 3/1 - 7")

    def test_to_dictionary(self):
        """Test dictionary export of Square."""
        s = Square(10, 2, 1, 1)
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
