#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list with max value at the start."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test calling function with no arguments returns None."""
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list of only negative numbers."""
        self.assertEqual(max_integer([-10, -5, -2, -8]), -2)

    def test_mixed_positive_negative(self):
        """Test a list with both positive and negative numbers."""
        self.assertEqual(max_integer([-10, 5, 0, -2]), 5)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_duplicate_max(self):
        """Test a list where the maximum value appears multiple times."""
        self.assertEqual(max_integer([5, 5, 2, 1]), 5)

    def test_string_list(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["apple", "zebra", "mango"]), "zebra")

    def test_single_string(self):
        """Test passing a single string."""
        self.assertEqual(max_integer("holberton"), "t")


if __name__ == "__main__":
    unittest.main()
