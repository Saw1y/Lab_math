import numpy as np


def diagonal(matrix):
    size = len(matrix)
    det = 1.0

    for i in range(size):
        ind = i
        while matrix[ind][i] == 0:
            det *= -1
            ind += 1
            if ind == size:
                return None

        matrix[[i, ind]] = matrix[[ind, i]]

        for j in range(i + 1, size):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, size * 2):
                matrix[j][k] -= factor * matrix[i][k]

    for i in range(size):
        det *= matrix[i][i]

    for i in range(size - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, size * 2):
                matrix[j][k] -= factor * matrix[i][k]

    return det, matrix


def expanded_matrix(A, B):
    size_a = np.shape(A)
    size_b = np.shape(B)
    cols = size_a[1] + size_b[1]
    rows = np.max((size_a[0], size_b[0]))

    matrix = np.zeros((rows, cols)).astype('float')

    matrix[0:size_a[0], 0:size_a[1]] = A
    matrix[0:size_b[0], size_a[1]:cols] = B

    return matrix


def inverse_matrix(matrix):
    rows = np.shape(matrix)[0]
    cols = rows * 2

    for i in range(rows):
        for j in range(rows, cols):
            matrix[i][j] /= matrix[i][i]

    return matrix


def norm(matrix):
    size = len(matrix)
    maxi = -float('inf')
    for i in range(size):
        summ = 0
        for j in range(size):
            summ += abs(matrix[i][j])
        if summ > maxi:
            maxi = summ

    return maxi


def make_diagonally_dominant(matrix, free):
    matrix = np.copy(matrix)
    free = np.copy(free)
    size = len(matrix)
    for i in range(size):
        max_row = max(range(i, size), key=lambda row: abs(matrix[row, i]))

        if max_row != i:
            matrix[[i, max_row]] = matrix[[max_row, i]]
            free[[i, max_row]] = free[[max_row, i]]

        for j in range(size):
            if i != j:
                factor = np.round(matrix[j, i] / matrix[i, i], 4)
                matrix[j] -= factor * matrix[i]
                free[j] -= factor * free[i]

    return matrix, free
