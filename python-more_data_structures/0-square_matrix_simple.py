#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    while (matrix):
        square_matrix = []
        for idx in matrix:
            square_matrix.append(list(map(lambda x: x*x, idx)))
        return (square_matrix)
