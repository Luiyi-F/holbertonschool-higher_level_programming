#!/usr/bin/python3
"""
Module base with Base class
"""


class Base():
    """
    Create Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization Bese class
        Args:
            id = None
        """
        if id is not None:
            self.id = id

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects