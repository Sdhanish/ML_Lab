import numpy as np
# Creating two matrices
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
matrix_b = np.array([[9, 8, 7],
                     [6, 5, 4],
                     [3, 2, 1]])
# Displaying the matrices
print("Matrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)
# Matrix addition
matrix_sum = matrix_a + matrix_b
print("\nMatrix Addition (A + B):")
print(matrix_sum)
# Matrix subtraction
matrix_diff = matrix_a - matrix_b
print("\nMatrix Subtraction (A - B):")
print(matrix_diff)
# Matrix multiplication
matrix_product = np.dot(matrix_a, matrix_b)
print("\nMatrix Multiplication (A * B):")
print(matrix_product)
# Element-wise multiplication
elementwise_product = matrix_a * matrix_b
print("\nElement-wise Multiplication (A * B):")
print(elementwise_product)
# Transpose of a matrix
matrix_transpose = matrix_a.T
print("\nTranspose of Matrix A:")
print(matrix_transpose)
