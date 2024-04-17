import numpy as np
#In lab task
num = np.ones((8, 8), dtype=int)
num[1:-1, 1:-1] = 0
print(num)

#post lab task
matrix = np.zeros((8, 8), dtype=int)
matrix[::2, ::2] = 0 
matrix[1::2, 1::2] = 0
matrix[::2, 1::2] = 1 
matrix[1::2, ::2] = 1
print(matrix)
