#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Helper function to calculate the determinant of a matrix
double determinant(vector<vector<double>>& matrix, int n) {
    if (n == 1) {
        return matrix[0][0];
    }

    double det = 0;
    vector<vector<double>> submatrix(n, vector<double>(n));

    for (int x = 0; x < n; x++) {
        int subi = 0; // Row index for submatrix
        for (int i = 1; i < n; i++) { // Start from 1 (exclude first row)
            int subj = 0; // Column index for submatrix
            for (int j = 0; j < n; j++) {
                if (j == x) continue; // Exclude current column
                submatrix[subi][subj] = matrix[i][j];
                subj++;
            }
            subi++;
        }
        det += pow(-1, x) * matrix[0][x] * determinant(submatrix, n - 1);
    }
    return det;
}

// Function to construct the Laplacian matrix
vector<vector<double>> constructLaplacianMatrix(const vector<vector<int>>& adjMatrix) {
    int n = adjMatrix.size();
    vector<vector<double>> laplacian(n, vector<double>(n, 0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                // Diagonal entry: degree of vertex
                int degree = 0;
                for (int k = 0; k < n; k++) {
                    degree += adjMatrix[i][k];
                }
                laplacian[i][i] = degree;
            } else if (adjMatrix[i][j] == 1) {
                // Off-diagonal entry: -1 if adjacent
                laplacian[i][j] = -1;
            } else {
                // Off-diagonal entry: 0 if not adjacent
                laplacian[i][j] = 0;
            }
        }
    }
    return laplacian;
}

// Function to remove the last row and column from the Laplacian matrix
vector<vector<double>> reduceMatrix(const vector<vector<double>>& matrix) {
    int n = matrix.size();
    vector<vector<double>> reducedMatrix(n - 1, vector<double>(n - 1));

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1; j++) {
            reducedMatrix[i][j] = matrix[i][j];
        }
    }
    return reducedMatrix;
}

// Function to compute the number of spanning trees using Kirchhoff's Matrix-Tree Theorem
int numberOfSpanningTrees(const vector<vector<int>>& adjMatrix) {
    // Step 1: Construct the Laplacian matrix
    vector<vector<double>> laplacian = constructLaplacianMatrix(adjMatrix);

    // Step 2: Remove the last row and last column
    vector<vector<double>> reducedLaplacian = reduceMatrix(laplacian);

    // Step 3: Compute the determinant of the reduced Laplacian matrix
    return round(determinant(reducedLaplacian, reducedLaplacian.size()));
}

int main() {
    // Example adjacency matrix
    vector<vector<int>> adjMatrix = {
        {0, 1, 1, 0},
        {1, 0, 1, 1},
        {1, 1, 0, 1},
        {0, 1, 1, 0}
    };

    cout << "Number of spanning trees: " << numberOfSpanningTrees(adjMatrix) << endl;

    return 0;
}

/*
### Kirchhoff's Matrix-Tree Theorem to Find Number of Spanning Trees

1. **Step 1: Construct the Laplacian Matrix**
   - Create a square matrix with rows and columns equal to the number of vertices.
   - Fill entries as follows:
       - If \(i = j\) (diagonal), \(L[i][i] =\) degree of vertex \(i\).
       - If \(i \neq j\) and \(i, j\) are adjacent, \(L[i][j] = -1\).
       - If \(i \neq j\) and \(i, j\) are not adjacent, \(L[i][j] = 0\).

2. **Step 2: Reduce the Matrix**
   - Remove the last row and last column from the Laplacian matrix to form the reduced Laplacian matrix.

3. **Step 3: Compute the Determinant**
   - Use a recursive function to compute the determinant of the reduced Laplacian matrix.
   - The determinant represents the number of spanning trees.

4. **Example Execution**
   Input Graph (Adjacency Matrix):
       0 -- 1 -- 2
        \   |   /
          -- 3 --

   Laplacian Matrix:
       [ 2, -1, -1,  0]
       [-1,  3, -1, -1]
       [-1, -1,  3, -1]
       [ 0, -1, -1,  2]

   Reduced Laplacian Matrix (Remove last row/column):
       [ 2, -1, -1 ]
       [-1,  3, -1 ]
       [-1, -1,  3 ]

   Determinant of Reduced Laplacian:
       det = 16

   Output:
       Number of spanning trees: 16

5. **Complexity**
   - Constructing Laplacian Matrix: \(O(V^2)\)
   - Determinant Calculation: \(O(N!)\) in the worst case (recursive determinant).
   - Total Complexity: Efficient for small to medium graphs.

6. **Use Case**
   - This algorithm efficiently calculates the number of spanning trees using linear algebra concepts.
*/
