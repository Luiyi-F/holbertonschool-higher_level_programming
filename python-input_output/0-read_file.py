#!/usr/bin/python3
"""
Module 0-read_file with read_file(filename="")
In this module read the contend of a file
"""


def read_file(filename=""):
    """
    Read a expecific file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
