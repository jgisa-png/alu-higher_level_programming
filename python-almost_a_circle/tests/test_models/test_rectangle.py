#!/usr/bin/python3
"""Unit tests for the Rectangle class in models/rectangle.py."""
from io import StringIO
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class functionality and validation."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_valid_instantiation(self):
        """Test valid Rectangle creation with default and custom values."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(4, 5, 1, 2, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)

    def test_invalid_types(self):
        """Test TypeError raised for non-integer attributes."""
        invalid_vals = ["2", 2.5, True, [1], {"a": 1}, (1,), None]
        for val in invalid_vals:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(val, 2)
            with self.assertRaisesRegex(TypeError,
                                        "height must be an integer"):
                Rectangle(2, val)
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(2, 2, val)
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(2, 2, 0, val)

    def test_invalid_values(self):
        """Test ValueError raised for out-of-range dimensions and offsets."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 2, 0, -1)

    def test_area(self):
        """Test area computation."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)
        r.width = 10
        r.height = 5
        self.assertEqual(r.area(), 50)

    def test_str(self):
        """Test __str__ output format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        """Test display output with and without x/y offsets."""
        r1 = Rectangle(2, 3)
        captured = StringIO()
        sys.stdout = captured
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n##\n")

        r2 = Rectangle(2, 2, 2, 1)
        captured = StringIO()
        sys.stdout = captured
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n  ##\n  ##\n")

    def test_update_args(self):
        """Test update method with positional *args."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update method with **kwargs and *args precedence."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(y=1, width=2, x=3, id=89, height=4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/4")
        r.update(50, width=99)
        self.assertEqual(r.id, 50)
        self.assertEqual(r.width, 2)

    def test_to_dictionary(self):
        """Test dictionary export of Rectangle."""
        r = Rectangle(10, 2, 1, 9, 1)
        expected = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
