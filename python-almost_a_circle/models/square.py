#!/usr/bin/python3
"""
Module square with Square class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Create Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization Square class
        Args:
            size
            x=0
            y=0
            id=None
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value

    def __str__(self):
        """Print message for see id, x & y and width & height"""
        cls_name = self.__class__.__name__
        msg_form = "[{}] ({:d}) {:d}/{:d} - {:d}"
        return msg_form.format(cls_name, self.id, self.x, self.y, self.width)
