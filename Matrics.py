import numpy as np

def get_matrix_from_input(rows, cols):
    """Reads a matrix from the keyboard with given dimensions."""
    print(f"Enter the elements of a {rows}x{cols} matrix:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print(f"Error: Please enter exactly {cols} elements per row.")
            return None
        matrix.append(row)
    return np.array(matrix)

def matrix_addition(A, B):
    """Perform matrix addition."""
    return A + B

def matrix_subtraction(A, B):
    """Perform matrix subtraction."""
    return A - B

def element_wise_multiplication(A, B):
    """Perform element-wise multiplication."""
    return A * B

def matrix_multiplication(A, B):
    """Perform matrix multiplication."""
    return np.dot(A, B)

# Main program
# Step 1: Define matrix dimensions
rows = int(input("Enter the number of rows for the matrices: "))
cols = int(input("Enter the number of columns for the matrices: "))

# Step 2: Read matrices from input
print("Matrix A:")
A = get_matrix_from_input(rows, cols)
print("Matrix B:")
B = get_matrix_from_input(rows, cols)

# Step 3: Check if matrices are valid for operations
if A is None or B is None:
    print("Invalid matrices. Exiting program.")
else:
    # Perform operations
    print("Matrix A + B:\n", matrix_addition(A, B))
    print("Matrix A - B:\n", matrix_subtraction(A, B))
    print("Element-wise A * B:\n", element_wise_multiplication(A, B))
    
    # Matrix multiplication requires A's columns to match B's rows
    if A.shape[1] == B.shape[0]:
        print("Matrix product A @ B:\n", matrix_multiplication(A, B))
    else:
        print("Matrix multiplication not possible due to incompatible")       