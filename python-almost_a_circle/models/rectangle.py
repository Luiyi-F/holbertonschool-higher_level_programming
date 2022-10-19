#!/usr/bin/python3
"""
Module rectangle with Rectangle class
"""
import sys
from .base import Base


class Rectangle(Base):
    """
    Create Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization method
        Args:
            width
            height
            x=0
            y=0
            id=None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Return area for Rectangle"""
        return self.__height * self.__width

    def display(self):
        """Print square"""
        for idx in range(self.__y):
            print()
        for idx2 in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, file=sys.stdout)

    def __str__(self):
        """Print message for see id, x & y and width & height"""
        cls_name = self.__class__.__name__
        msg_form = "[{}] ({}) {}/{} - {}/{}"
        return msg_form.format(cls_name, self.id, self.__x, self.__y,
                               self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Args function"""
        args_list = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for idx in range(len(args)):
                setattr(self, args_list[idx], args[idx])

    def to_dictionary(self):
        """Returns dictionary function"""
        Rec_dict = {"id": self.id,
                    "width": self.__width,
                    "height": self.__height,
                    "x": self.__x, "y": self.__y}
        return Rec_dict
