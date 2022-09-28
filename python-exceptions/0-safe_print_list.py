#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    value = 0
    try:
        for idx in range(x):
            print("{}".format(my_list[idx]), end="")
            value += 1
    except (ValueError):
        pass
    finally:
        print("")
        return (value)