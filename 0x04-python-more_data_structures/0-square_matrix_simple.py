#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [list(row) for row in matrix]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] *= new_matrix[i][j]
    return new_matrix
