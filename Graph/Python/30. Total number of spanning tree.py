# Helper function to calculate the determinant of a matrix
def determinant(matrix, n):
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    det = 0
    submatrix = [[0] * n for _ in range(n)]
    for x in range(n):
        # Row index for submatrix
        subi = 0
        # Start from 1 (exclude first row)
        for i in range(1, n):
            # Column index for submatrix
            subj = 0
            for j in range(n):
                # Exclude current column
                if j == x:
                    continue
                submatrix[subi][subj] = matrix[i][j]
                subj += 1
            subi += 1
        det += (-1) ** x * matrix[0][x] * determinant(submatrix, n - 1)
    return det


# Function to construct the Laplacian matrix
def constructLaplacianMatrix(adjMatrix):
    n = len(adjMatrix)
    laplacian = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                # Diagonal entry: degree of vertex
                degree = 0
                for k in range(n):
                    degree += adjMatrix[i][k]
                laplacian[i][i] = degree
            elif adjMatrix[i][j] == 1:
                # Off-diagonal entry: -1 if adjacent
                laplacian[i][j] = -1
            else:
                # Off-diagonal entry: 0 if not adjacent
                laplacian[i][j] = 0
    return laplacian


# Function to remove the last row and column from the Laplacian matrix
def reduceMatrix(matrix):
    n = len(matrix)
    reducedMatrix = [[0] * (n - 1) for _ in range(n - 1)]
    for i in range(n - 1):
        for j in range(n - 1):
            reducedMatrix[i][j] = matrix[i][j]
    return reducedMatrix


# Function to compute the number of spanning trees using Kirchhoff's Matrix-Tree Theorem
def numberOfSpanningTrees(adjMatrix):
    if not adjMatrix:
        return 0
    # Step 1: Construct the Laplacian matrix
    laplacian = constructLaplacianMatrix(adjMatrix)
    # Step 2: Remove the last row and last column
    reducedLaplacian = reduceMatrix(laplacian)
    # Step 3: Compute the determinant of the reduced Laplacian matrix
    return round(determinant(reducedLaplacian, len(reducedLaplacian)))


def main():
    adjMatrix = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
    print("Number of spanning trees:", numberOfSpanningTrees(adjMatrix))


if __name__ == "__main__":
    main()


'''
Let n be vertices and d=n-1 the reduced determinant dimension.
Time: O(n^2 + d!): Laplacian/minor construction is quadratic, while
cofactor expansion branches d ways, then d-1, etc. Recurrence
T(d)=d*T(d-1)+O(d^3) has factorial growth; no elimination optimization.
Space: O(n^3) auxiliary worst case: recursive levels retain matrices
of sizes d^2, (d-1)^2, ... whose sum is cubic.
Assumes a simple undirected graph. Floating-point rounding, as in C++,
can lose accuracy for large counts; an empty minor has determinant 1.
'''
