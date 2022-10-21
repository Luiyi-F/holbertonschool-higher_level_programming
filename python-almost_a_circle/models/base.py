#!/usr/bin/python3
"""
Module base with Base class
"""


import json


class Base():
    """
    Create Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization method
        Args:
            id = None
        """
        if id is not None:
            self.id = id

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return dictionary how string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """String JSON to file"""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(
                [cls.to_dictionary(x) for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Return json string"""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to instance"""
        if cls.__name__ is "Rectangle":
            instance = cls(1, 1)
        if cls.__name__ is "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """File instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                a_list = cls.from_json_string(f.read())
                return [cls.create(**idx) for idx in a_list]
        except IOError:
            return []
