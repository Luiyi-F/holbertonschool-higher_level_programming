#!/usr/bin/python3
"""
Wirte a class Square that defines a square by:(based on 1-square.py)
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
    size must be an integer, otherwise raise a TypeError exception with
    the message size must be an integer
    if size is less than 0, raise a ValueError exception with the message
    size must be >= 0
"""


class Square:
    """initalization class Squiare"""

    def __init__(self, size=0):
        """Valitation if the size is to
         integer or is a negative number"""
        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        if int(size) < 0:
            raise (ValueError("size must be >= 0"))
        self.__size = size
