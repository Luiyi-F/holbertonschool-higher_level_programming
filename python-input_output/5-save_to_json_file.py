#!/usr/bin/python3
"""
Module 5-save_to_json_file with save_to_json_file(my_obj, filename)
Writes an object(data struct) to txt
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to txt, with JSON representation
    Arguments: my_obj, filename
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
