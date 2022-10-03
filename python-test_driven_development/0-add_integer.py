#!/usr/bin/python3
"""
This is the adds integer module.

This module supplies one function, add_integer().
For example:

>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """
    Given a two arguments (a and b) and add these
    Return the sum between a and b, this is a integer 
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a + b))
