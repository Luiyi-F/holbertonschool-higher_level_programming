#!/usr/bin/python3
"""
Module is same class with is_same_class() function:
return True if the object is isntace of the class,
otherwise False

Example:
>>> is_same_class(4, int):
True
>>> is_same_class("4", int):
False
"""


def is_same_class(obj, a_class):
    """
    Return True if the object is instance
    of the class
    
    Arguments: Object(obj), object class(a_class)
    """
    return type(obj) is a_class
