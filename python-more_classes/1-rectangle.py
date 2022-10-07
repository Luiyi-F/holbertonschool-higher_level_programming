#!/usr/bin/python3
"""
Module with Class Rectangle
"""


class Rectangle:
    """Initialization Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Method: Rectangle object
        Args: Width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """setter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """getter"""
        if not isinstance(value, int):
            raise (TypeError("width must be an integer"))
        if value < 0:
            raise (ValueError("width must be >= 0"))
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if not isinstance(value, int):
            raise (TypeError("height must be an integer"))
        if value < 0:
            raise (ValueError("height must be >= 0"))
        self.__height = value
