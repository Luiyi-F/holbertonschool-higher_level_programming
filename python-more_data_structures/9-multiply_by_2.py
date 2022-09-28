#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    square_dict = {}
    
    for key in a_dictionary:
        square_dict[key] = a_dictionary[key] * 2
    return (square_dict)
