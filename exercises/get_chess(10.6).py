import numpy as np

def get_chess(a):
    matrix = np.zeros((a, a))
    matrix[1::2, ::2] = 1
    matrix[::2, 1::2] = 1
    return matrix
    print(matrix)

print(get_chess(4))