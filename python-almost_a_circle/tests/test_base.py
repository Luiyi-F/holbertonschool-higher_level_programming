#!/usr/bin/python3
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Initialization Test base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_MissId(self):
        """Missing id assignation"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_intId(self):
        """Integer id assignation"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_NegIntId(self):
        """Negative integer id assignation"""
        b = Base(-12)
        self.assertEqual(b.id, -12)
