#!/usr/bin/python3
"""
Module rectangle with Rectangle class
"""
from .base import Base


class Rectangle(Base):
    """
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization method
        Args:
            width
            height
            x = 0
            y = 0
            id = None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y