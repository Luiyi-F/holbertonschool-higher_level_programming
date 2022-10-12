#!/usr/bin/python3
"""
Module 2-append_write with def append_write(filename="", text=""):
In this module write a text of a file and add more text
"""


def append_write(filename="", text=""):
    """
    Write a text in the file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)

    return (len(text))
