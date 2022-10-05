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
        raise (TypeError("text must be a string"))

    for chars in range(len(text)):
        if text[chars] == ' ' and\
                text[chars - 1] == '.' or\
                text[chars - 1] == '?' or\
                text[chars - 1] == ':':
            continue
        print(text[chars], end="")
        if text[chars] == '.' or\
                text[chars] == '?' or\
                text[chars] == ':':
            print("\n")
