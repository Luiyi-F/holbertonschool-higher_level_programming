#!/usr/bin/python3
"""
Module 3-to_json_string with to_json_string(my_obj) function
Return the json file of a object
"""
import json


def to_json_string(my_obj):
    """
    Return the json file for one object
    """
    return (json.dumps(my_obj))
