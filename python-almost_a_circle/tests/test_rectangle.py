#!/usr/bin/python3
"""
Rectangle test
"""
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Initialization Test base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_IntId(self):
        """Integer id assignation"""
        r = Rectangle(12, 4)
        self.assertEqual(r.id, 1)

        r1 = Rectangle(12, 4, 1)
        self.assertEqual(r1.id, 1)

    def test_IntId2(self):
        """Integer id assignation"""
        r2 = Rectangle(12, 4, 1, 1)
        self.assertEqual(r2.id, 1)

        r3 = Rectangle(12, 4, 1, 1, 5)
        self.assertEqual(r3.id, 5)

    def test_NegParameter(self):
        """Negative integer in parameter assignation"""
        with self.assertRaises(ValueError):
            r = Rectangle(-12, 4)

        with self.assertRaises(ValueError):
            r = Rectangle(12, -4)

    def test_StrParameter(self):
        """string in parameter assignation"""
        with self.assertRaises(TypeError):
            r = Rectangle('12', 4)

        with self.assertRaises(TypeError):
            r = Rectangle(12, '4')

        with self.assertRaises(TypeError):
            r = Rectangle(12, 4, '1')

        with self.assertRaises(TypeError):
            r = Rectangle(12, 4, '1')

        with self.assertRaises(TypeError):
            r = Rectangle(12, 4, 1, '1')

        with self.assertRaises(TypeError):
            r = Rectangle(12, 4, 1, 1, '5')


if __name__ == '__main__':
    unittest.main()
