import numpy as np
a = 9
b = 8
matrix = np.zeros((a, b))
#print(matrix)
#print(matrix[::2])
#matrix1 = matrix[::2] +=1
#print(matrix1)


x = np.zeros((a, a))
print(x)
x[:, 1::2] = [1]
print(x)
