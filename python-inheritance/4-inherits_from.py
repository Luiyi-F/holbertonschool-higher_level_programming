#!/usr/bin/python3
"""
Module is kind of class with is_kind_of_class() function:
return True if the object is isntace of the class directly
or inderectly; otherwise False

Example:
>>> inherits_from(4, int):
True
>>> inherits_from(4, object):
True
"""


def inherits_from(obj, a_class):
    """Return True if the object is a instance
        directly or indirectly of a class
    Arguments: Object(obj), object class(a_class)"""
    return isinstance(obj, a_class)
