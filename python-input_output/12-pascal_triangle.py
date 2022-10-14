#!/usr/bin/python3
"""
Mudule 12-pascal_triangle with pascal_trinagle(n)
Return list with form a triangle
"""
def pascal_triangle(n):
    """
    Return a list of pascal trinagle
    """
    new_l = []
    for idx in range(n):
        new_l.append([])
        for idx2 in range(idx + 1):
            if idx2 == 0 or idx2 == idx:
                new_l[idx].append(1)
            else:
                new_l[idx].append(new_l[idx - 1][idx2 - 1] +
                                  new_l[idx - 1][idx2])
    return (new_l)
