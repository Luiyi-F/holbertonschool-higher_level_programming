#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = {key: value for key, value in sorted(a_dictionary.items())}
    for dict_key, dict_value in sorted_dict.items():
        print("{} {}". format(dict_key, dict_value))
