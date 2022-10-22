#!/usr/bin/python3
"""
Rectangle test
"""
import unittest
import sys
import io

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
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.id, 1)

        r1 = Rectangle(12, 4, 1)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(12, 4, 1, 1)
        self.assertEqual(r2.id, 3)
        r3 = Rectangle(12, 4, 1, 1, 5)
        self.assertEqual(r3.id, 5)

    def test_NegParameter(self):
        """Negative integer in parameter assignation"""
        with self.assertRaises(ValueError):
            r = Rectangle(-12, 4)
        with self.assertRaises(ValueError):
            r1 = Rectangle(12, -4)
        with self.assertRaises(ValueError):
            r = Rectangle(12, 4, -1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(12, 4, 1, -1)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 4)
        with self.assertRaises(ValueError):
            r3 = Rectangle(12, 0)

    def test_StrParameter(self):
        """string in parameter assignation"""
        with self.assertRaises(TypeError):
            r = Rectangle('12', 4)

        with self.assertRaises(TypeError):
            r1 = Rectangle(12, '4')

        with self.assertRaises(TypeError):
            r2 = Rectangle(12, 4, '1')

        with self.assertRaises(TypeError):
            r3 = Rectangle(12, 4, 1, '1')

    def test_Area(self):
        """Result area function"""
        r = Rectangle(12, 4)
        self.assertEqual(r.area(), 48)

    def test__Str__(self):
        """Result str function"""
        r = Rectangle(12, 4, 1, 1, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 1/1 - 12/4")

    def test_Inhertans(self):
        r = Rectangle(12, 4)
        self.assertEqual(True, isinstance(r, Base))

    def test_Dictionary(self):
        r = Rectangle(12, 4, 1, 1, 5)
        self.assertEqual(r.to_dictionary(), {
                         'width': 12, 'height': 4, 'x': 1, 'y': 1, 'id': 5})

    def test_Display(self):
        """Test for display"""
        output = io.StringIO()
        sys.stdout = output
        Rectangle(2, 2, 1, 1).display()
        self.assertEqual(output.getvalue(), '##\n##\n')

    def test_Update(self):
        """Result update"""
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(50, 12, 4, 11, 11)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 11)
        self.assertEqual(r.y, 11)
        self.assertEqual(r.id, 50)

    def test_UpdateKwargs(self):
        """Result kwargs"""
        r = Rectangle(1, 1, 1, 1)
        r.update(x=11, height=4, width=12, y=11)
        self.assertEqual(r.width, 12)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 11)
        self.assertEqual(r.y, 11)
        self.assertEqual(r.id, 1)

    def test_RectangleCreate3(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)


if __name__ == '__main__':
    unittest.main()
