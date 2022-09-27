#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    square_dict = {}
    if (a_dictionary):
        for key, value in a_dictionary.items():
            square_dict.update({key: value * 2})
        return (square_dict)
