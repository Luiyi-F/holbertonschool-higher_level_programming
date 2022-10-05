#!/usr/bin/python3
"""
This is the 5-text_indentation module.

This module supplies one function, text_indention().
For example:

>>> text_indentation(""Lorem ipsum dolor sit amet,\
    consectetur adipiscing elit."")

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

"""


def text_indentation(text):
    """
    Given one argument (it`s a text)
    Return indentation text
    """
    delim = [".", "?", ":"]
    skip_next = False

    if not isinstance(text, str):
        raise (TypeError("text must be a string"))

    for indx in text:
        if indx in delim:
            print(indx), print()
            skip_next = True
        else:
            if skip_next is False:
                print(indx, end="")
            else:
                if indx != " ":
                    print(indx, end="")
                    skip_next = False
