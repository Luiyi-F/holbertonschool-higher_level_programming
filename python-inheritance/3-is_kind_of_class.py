#!/usr/bin/python3
"""
Module is kind of class with is_kind_of_class() function:
return True if the object is isntace of the class,
otherwise False

Example:
>>> def is_kind_of_class(4, int):
True
>>> is_kind_of_class(4, object):
True
"""


def is_kind_of_class(obj, a_class):
    """Return True if the object is instance
    of the class
    Arguments: Object(obj), object class(a_class)"""
    return isinstance(obj, a_class)
