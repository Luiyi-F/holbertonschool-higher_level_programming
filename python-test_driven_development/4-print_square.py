#!/usr/bin/python3
"""
This is the print square module.

This module supplies one function, print_square().
For example:

>>> print_square(4)

####
####
####
####
"""


def print_square(size):
    """
    Given one argument, this is a lenght of the square
    Return prints lenght of the square
    """
    if not isinstance(size, int) or type(size) is float\
            and size < 0:
        raise (TypeError("size must be an integer"))

    if size < 0:
        raise (ValueError("size must be >= 0"))

    for height in range(size):
        for width in range(size):
            print("#", end="")
        print().
