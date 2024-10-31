#include <iostream>
#include <vector>
#include <algorithm> // For std::reverse
using namespace std;

// Function to transpose only the lower half of the matrix
void transposeLowerHalf(vector<vector<int>>& matrix) {
    int n = matrix.size();

    // Swap elements in the lower triangle (i > j) to transpose the lower half
    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
}

// Function to rotate the matrix 90 degrees clockwise after transposing
void rotate90Clockwise(vector<vector<int>>& matrix) {
    int n = matrix.size();

    // Step 1: Transpose only the lower half of the matrix
    transposeLowerHalf(matrix);

    // Step 2: Reverse each row to achieve a 90-degree clockwise rotation
    for (int i = 0; i < n; ++i) {
        reverse(matrix[i].begin(), matrix[i].end());
    }
}

// Function to print the matrix for verification
void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int element : row) {
            cout << element << " ";
        }
        cout << endl;
    }
}

int main() {
    // Example 4x4 matrix
    vector<vector<int>> matrix = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    cout << "Original Matrix:\n";
    printMatrix(matrix);

    // Rotate the matrix 90 degrees clockwise
    rotate90Clockwise(matrix);

    cout << "\nMatrix after 90-degree clockwise rotation:\n";
    printMatrix(matrix);

    return 0;
}
