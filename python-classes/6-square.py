#!/usr/bin/python3
"""
Square Class
"""


class Square:
    """initalization class Squiare"""

    def __init__(self, size=0, position=(0, 0)):
        """Method: Square object
        args: size of the square"""

        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        if int(size) < 0:
            raise (ValueError("size must be >= 0"))

        if not isinstance(position, tuple) or len(position) != 2 \
                or not all(isinstance(number, int) for number in position)\
                or not all(number >= 0 for number in position):
            raise (TypeError("position must be a tuple of 2 positive integers"))

        self.__position = position
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise (TypeError("size must be an integer"))
        if int(value) < 0:
            raise (ValueError("size must be >= 0"))

        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(number, int) for number in value)\
                or not all(number >= 0 for number in value):
            raise (TypeError("position must be a tuple of 2 positive integers"))

        self.__position = value

    def area(self):
        """Return area of the Square"""
        area_sqr = self.__size**2
        return (area_sqr)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for indx in range(self.__position[1]):
            print()
        for indx in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
