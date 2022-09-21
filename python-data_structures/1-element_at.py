#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list):
        return (None)
    for number in range(0, len(my_list)):
        if number == idx:
            return (my_list[number])
