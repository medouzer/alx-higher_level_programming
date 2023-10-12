#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(row) for row in matrix]
    for j in range(len(new_matrix)):
        for i in range(len(new_matrix)):
            new_matrix[j][i] = new_matrix[j][i] ** 2
    return new_matrix
