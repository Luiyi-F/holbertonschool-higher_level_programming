#!/usr/bin/python3
"""
Module 1-write_file with read_file(filename="", text=")
In this module write a text of a file
"""


def write_file(filename="", text=""):
    """
    Write a text in the file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)

    return (len(text))
