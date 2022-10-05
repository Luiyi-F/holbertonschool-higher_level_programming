#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test file for the function Max_integer()
    in different cases"""
    def test_maxint(self):
        # Test max_integer when list >= 0
        self.assertAlmostEqual(max_integer([0]), 0)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([10, 34, 12, 15]), 34)
