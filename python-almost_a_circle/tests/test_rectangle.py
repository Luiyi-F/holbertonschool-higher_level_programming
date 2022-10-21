#!/usr/bin/python3
import string
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Initialization Test base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_intId(self):
        """Integer id assignation"""
        r = Rectangle(12, 4)
        self.assertEqual(r.id, 1)

        r2 = Rectangle(12, 4, 1, 1, 5)
        self.assertEqual(r2.id, 5)

    def test_NegParameter(self):
        """Negative integer in parameter assignation"""
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(10, -2)

    def test_StrParameter(self):
        """string in parameter assignation"""
        with self.assertRaises(TypeError):
            r = Rectangle('10', 2)

        with self.assertRaises(TypeError):
            r = Rectangle(10, '2')
