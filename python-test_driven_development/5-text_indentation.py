#!/usr/bin/python3
"""
This is the 5-text_indentation module.

This module supplies one function, text_indention().
For example:

>>> text_indentation(""Lorem ipsum dolor sit amet, consectetur adipiscing elit."")

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

"""


def text_indentation(text):
    """
    Given one argument (it`s a text)
    Return indentation text
    """
    if not isinstance(text, str):
        raise (TypeError("text mus be a string"))

    for indx in range(len(text)):
        if text[indx] == ' ' and \
                text[indx - 1] == '.' or \
                text[indx - 1] == '?' or \
                text[indx - 1] == ':':
            continue

        print(text[indx], end="")
        if text[indx] == '.' or \
                text[indx] == '?' or \
                text[indx] == ':':
            print("\n")
