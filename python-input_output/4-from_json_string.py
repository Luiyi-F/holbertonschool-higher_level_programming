#!/usr/bin/python3
"""
Module 4-from_json_string with from_json_string(my_str) function
Return the json file of a string
"""
import json


def from_json_string(my_str):
    """
    Return the json file for one object
    """
    return (json.loads(my_str))
