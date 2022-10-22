#!/usr/bin/python3
"""
Rectangle test
"""
import unittest
import sys
import io
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Initialization Test base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_IntId(self):
        """Integer id assignation"""
        rq = Square(12, 4)
        self.assertEqual(rq.size, 12)
        self.assertEqual(rq.x, 4)

        rq1 = Square(12, 4, 3)
        self.assertEqual(rq1.size, 12)
        self.assertEqual(rq1.x, 4)
        self.assertEqual(rq1.y, 3)

        rq2 = Square(12, 4, 3, 2)
        self.assertEqual(rq2.size, 12)
        self.assertEqual(rq2.x, 4)
        self.assertEqual(rq2.y, 3)
        self.assertEqual(rq2.id, 2)

    def test_NegParameter(self):
        """Negative integer in parameter assignation"""
        with self.assertRaises(ValueError):
            sq = Square(-12, 4)
        with self.assertRaises(ValueError):
            sq = Square(12, -4)
        with self.assertRaises(ValueError):
            sq = Square(12, 4, -1)
        with self.assertRaises(ValueError):
            sq = Square(0, 4)
        with self.assertRaises(ValueError):
            sq = Square(0)

    def test_StrParameter(self):
        """string in parameter assignation"""
        with self.assertRaises(TypeError):
            sq = Square('12', 4)
        with self.assertRaises(TypeError):
            sq = Square(12, '4')
        with self.assertRaises(TypeError):
            sq = Square(12, 4, '1')

    def test_Representation(self):
        """Test Area"""
        sq = Square(7, id=1)
        self.assertEqual(sq.__str__(), "[Square] (1) 0/0 - 7")

    def test_Update(self):
        """Result update"""
        sq = Square(1, 1, 1, 1)
        sq.update(11, 11, 11, 11)
        self.assertEqual(sq.size, 11)
        self.assertEqual(sq.x, 11)
        self.assertEqual(sq.y, 11)
        self.assertEqual(sq.id, 11)

    def test_RectangleCreate3(self):
        sq = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)

    def test_save_to_empty(self):
        Square.save_to_file([])

        with open("Square.json", 'r', encoding="utf-8") as f:
            self.assertEqual(f.read(), '[]')
        os.remove("Square.json")

    def test_save_exists(self):
        Square.save_to_file([Square(2, 4, 6)])

        with open("Square.json", 'r') as f:
            self.assertEqual(
                f.read(), '[{"id": 1, "size": 2, "x": 4, "y": 6}]')
        os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
