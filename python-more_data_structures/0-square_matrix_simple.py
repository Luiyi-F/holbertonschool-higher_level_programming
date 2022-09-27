#!/usr/bin/python3
from re import M
from subprocess import list2cmdline


def square_matrix_simple(matrix=[]):
    while (matrix):
        square_matrix=[]
        for idx in matrix:
            square_matrix.append(list(map(lambda x: x*x, idx)))
        return (square_matrix)
