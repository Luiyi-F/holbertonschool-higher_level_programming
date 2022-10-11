#!/usr/bin/python3
"""
Module lookup with lookup() function:
return all available attributes and methods of a object
in to list

Example:
>>> lookup(int):
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', 
'__class__', '__delattr__', '__dir__', '__divmod__', '__doc__',
....]
"""


def lookup(obj):
    """Return attributes and methods of a object
    Arguments: object(obj)"""
    return (dir(obj))
