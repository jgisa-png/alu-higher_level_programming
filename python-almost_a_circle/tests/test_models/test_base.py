#!/usr/bin/python3
"""Unit tests for the Base class in models/base.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class functionality."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up generated JSON and CSV files."""
        for fname in ["Rectangle.json", "Square.json", "Base.json",
                      "Rectangle.csv", "Square.csv"]:
            if os.path.exists(fname):
                os.remove(fname)

    def test_auto_id(self):
        """Test automatic ID assignment increments properly."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_explicit_id(self):
        """Test explicit ID assignment."""
        b1 = Base(12)
        b2 = Base(-5)
        b3 = Base(0)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, -5)
        self.assertEqual(b3.id, 0)

    def test_mixed_ids(self):
        """Test alternating auto and explicit IDs."""
        b1 = Base()
        b2 = Base(89)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 89)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """Test serialization of list of dicts to JSON string."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{"id": 1, "width": 10}]
        json_str = Base.to_json_string(d)
        self.assertIsInstance(json_str, str)
        self.assertEqual(Base.from_json_string(json_str), d)

    def test_from_json_string(self):
        """Test deserialization of JSON string to list of dicts."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        s = '[{"id": 89, "width": 10, "height": 4}]'
        res = Base.from_json_string(s)
        self.assertEqual(res, [{"id": 89, "width": 10, "height": 4}])

    def test_save_and_load_file_rectangle(self):
        """Test save_to_file and load_from_file for Rectangle."""
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))
        self.assertEqual(str(loaded[1]), str(r2))
        self.assertIsNot(loaded[0], r1)

    def test_save_and_load_file_square(self):
        """Test save_to_file and load_from_file for Square."""
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])
        s1 = Square(5, 1, 2, 10)
        Square.save_to_file([s1])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(str(loaded[0]), str(s1))

    def test_create(self):
        """Test creating instances from dictionaries."""
        r1 = Rectangle(3, 5, 1, 2, 9)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

        s1 = Square(4, 2, 3, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_csv_serialization(self):
        """Test save_to_file_csv and load_from_file_csv."""
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])
        rects = Rectangle.load_from_file_csv()
        self.assertEqual(len(rects), 2)
        self.assertEqual(str(rects[0]), str(r1))
        self.assertEqual(str(rects[1]), str(r2))

        s1 = Square(5, 9, 1, 6)
        Square.save_to_file_csv([s1])
        squares = Square.load_from_file_csv()
        self.assertEqual(len(squares), 1)
        self.assertEqual(str(squares[0]), str(s1))


if __name__ == "__main__":
    unittest.main()
