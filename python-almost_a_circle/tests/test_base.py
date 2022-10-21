#!/usr/bin/python3
import string
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Initialization Test base class"""

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

    def test_StrId(self):
        """string id assignation"""
        b = Base("Id")
        self.assertEqual(b.id, "Id")

    def test_to_json_string(self):
        """to json string"""
        string = Base.to_json_string(None)
        self.assertEqual(string, "[]")

    def test_from_json_string(self):
        string = Base.from_json_string(None)
        self.assertEqual(string, [])
