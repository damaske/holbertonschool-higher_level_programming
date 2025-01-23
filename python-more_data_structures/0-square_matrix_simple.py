#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for r in matrix:
        square.append(r[:])
    for i in range(len(square)):
        for k in range(len(square[i])):
            square[i][k] = square[i][k] ** 2
    return square
