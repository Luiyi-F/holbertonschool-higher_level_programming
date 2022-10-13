#!/usr/bin/python3
"""
Module 9-student with Student class
Initialization for first_name, last_name and age
Return dictionary for the object
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialization class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return description of the dictionary
        for JSON searilaztion
        verification if attrs is a list
        """
        if type(attrs) is list and all([type(idx) == str for idx in attrs]):
            return {lr: lr_2 for lr, lr_2 in self.__dict__.items() if lr in attrs}

        return (self.__dict__)
