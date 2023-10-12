#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(row) for row in matrix]
    for a in range(len(new_matrix)):
        for i in range(len(new_matrix)):
            new_matrix[a][i] *= new_matrix[a][i]
    return new_matrix
