#!/usr/bin/python3
"""
Module 8-class_to_json with class_to_json(obj)
Return the dictionary description with simple
data structure
"""


def class_to_json(obj):
    """
    Return description of the dictionary
    for JSON searilaztion
    """
    return(obj.__dict__)
