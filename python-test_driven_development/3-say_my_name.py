#!/usr/bin/python3
"""
This is the Say may name module.

This module supplies one function, say_my_name().
For example:

>>> say_my_name("John", "Smith")
My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """
    Given two arguments first name and last name
    (both string)
    Return a message with both string
    """
    if type(first_name) is not str:
        raise (TypeError("first_name must be a string"))

    if type(last_name) is not str:
        raise (TypeError("last_name must be a string"))

    return (print("My name is {} {}".format(first_name, last_name)))
