# Function to transpose only the lower half of the matrix
def transposeLowerHalf(matrix):
    n = len(matrix)

    # Swap elements in the lower triangle (i > j)
    # to transpose the matrix
    for i in range(1, n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# Function to rotate the matrix 90 degrees clockwise
def rotate90Clockwise(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    transposeLowerHalf(matrix)

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


# Function to print the matrix
def printMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


# Example 4x4 matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Original Matrix:")
printMatrix(matrix)

# Rotate the matrix 90 degrees clockwise
rotate90Clockwise(matrix)

print("\nMatrix after 90-degree clockwise rotation:")
printMatrix(matrix)


'''
Time Complexity:
O(n^2)

Reason:

Step 1:
Transposing the matrix visits approximately half of the matrix.

The loops are:

for i in range(1, n):
    for j in range(i):

This performs approximately:

n * (n - 1) / 2

swaps.

Therefore, transpose takes:
O(n^2)


Step 2:
We reverse every row.

There are n rows and each row contains n elements.

Therefore:
O(n^2)


Overall Time Complexity:
O(n^2)


Space Complexity:
O(1)

Reason:

The rotation is performed in-place.

We do not create another n x n matrix.

Only temporary variables are used while swapping/reversing.

Therefore, auxiliary space complexity is:
O(1)
'''