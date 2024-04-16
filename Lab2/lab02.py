import numpy as np
print('********************* Lab 02 *****************************')
print('********************* In Lab Task *****************************')
num = np.ones((4, 4), dtype=int)
#set the inner elements to 0
num[1:-1, 1:-1] = 0
print(num)

print("\n")
print('********************* Post Lab Task *****************************')
#creating 8by8 matrix filled with zeros
matrix = np.zeros((8, 8), dtype=int)
#filling the matrix with the checkerboard pattern
matrix[::2, ::2] = 0 
matrix[1::2, 1::2] = 0
matrix[::2, 1::2] = 1 
matrix[1::2, ::2] = 1
print(matrix)
