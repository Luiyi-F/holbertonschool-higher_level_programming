#!/usr/bin/python3
"""
Module 6-load_from_json_file with load_from_json_file(filename)
Creates an object from JSON file
"""
import json


def load_from_json_file(filename):
    """
    Create object with JSON file
    Arguments: filename
    """
    with open(filename, encoding="utf-8") as file:
        return json.loads(file)
