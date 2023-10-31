#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a non-empty matrix (list of lists) of integers/floats")
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    for row in matrix:
        if not isinstance(row, list) or len(row) != num_cols:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    result_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        result_matrix.append(new_row)
    
    return result_matrix
