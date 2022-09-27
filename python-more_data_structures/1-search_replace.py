#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_num = my_list
    for indx, item in enumerate(my_list):
        if item == search:
            replace_num[indx] = replace
    return (replace_num)
